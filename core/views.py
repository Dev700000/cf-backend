from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BusinessType
from .gemini import generate_from_gemini
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def business_types_list(request):
    tipos = BusinessType.objects.all().values('id', 'name')
    return Response(list(tipos))

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Login que devuelve token JWT
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "email": user.email
        })

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Usuario creado exitosamente.",
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def generate_publication(request):
    permission_classes = [AllowAny]
    if request.method == 'POST':
        data = json.loads(request.body)
        business_type = data.get('business_type')
        business_name = data.get('business_name')
        tone = data.get('tone')
        date_today = date.today().strftime("%Y-%m-%d")
        if not business_type or not tone:
            return JsonResponse({'error': 'Faltan campos'}, status=400)

        prompt = (
            f"Eres un experto en marketing digital y redacción creativa. "
            f"Tu tarea es crear una publicación atractiva, original y en español para un negocio nombre '{business_name}' de tipo '{business_type}'. "
            f"El tono debe ser '{tone}', adaptado al estilo de comunicación de redes sociales como Facebook e Instagram. "
            f"Incluye emojis cuando sea apropiado, un llamado a la acción (CTA) claro, y un lenguaje cercano y persuasivo. "
            f"La publicación debe captar la atención en los primeros segundos y tener entre 2 y 4 párrafos. "
            f"No repitas palabras ni frases. Crea contenido que tenga que ver con la fecha '{date_today}' actual de cada mes "
            f"Evita hashtags por ahora. "
            f"Solo responde con el texto final de la publicación, sin explicaciones ni introducciones."
        )

        result = generate_from_gemini(prompt)

        return JsonResponse({'content': result})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)