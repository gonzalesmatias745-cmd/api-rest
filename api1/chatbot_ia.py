from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@api_view(['POST'])
def chatbot_ia(request):
    mensaje = request.data.get('mensaje', '')

    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje}]
    )

    texto = respuesta.choices[0].message.content
    return Response({"respuesta": texto})
