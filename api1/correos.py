from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

@api_view(['POST'])
def enviar_correo(request):
    correo = request.data.get('correo')
    asunto = request.data.get('asunto')
    mensaje = request.data.get('mensaje')

    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,   # remitente
        [correo],                   # destinatario
        fail_silently=False,
    )

    return Response({"status": "Correo enviado"})
