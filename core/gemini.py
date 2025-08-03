import google.generativeai as genai
import os

# Asegúrate de tener esta variable en tu entorno o config de Django
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_from_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al generar contenido: {str(e)}"
