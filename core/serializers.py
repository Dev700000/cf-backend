import profile
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import BusinessType, UserProfile  # Asegúrate de que UserProfile está importado

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True, label="Confirmar contraseña")
    business_name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    business_type = serializers.PrimaryKeyRelatedField(
        queryset=BusinessType.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'business_name', 'business_type']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya está registrado.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
        return data

    def create(self, validated_data):
        business_name = validated_data.pop('business_name', '')
        business_type = validated_data.pop('business_type', None)
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'business_name': business_name,
                'business_type': business_type
            }
        )
        if not created:
            profile.business_name = business_name
            profile.business_type = business_type
            profile.save()

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'business_name', 'business_type', 'business_description', 'content_goal']

