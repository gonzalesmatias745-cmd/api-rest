from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot(request):
    mensaje = request.data.get('mensaje', '').lower()

    if "hola" in mensaje:
        respuesta = "¡Hola! ¿En qué puedo ayudarte?"
    elif "sensor" in mensaje:
        respuesta = "Puedes consultar los sensores en /api/sensores/"
    elif "correo" in mensaje:
        respuesta = "Puedes enviar un correo en /api/correo/"
    else:
        respuesta = "No entendí eso. ¿Puedes repetirlo?"

    return Response({"respuesta": respuesta})
