from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, RolViewSet, SensorViewSet, LecturaSensorViewSet
from .chatbot import chatbot
from .chatbot_ia import chatbot_ia
from .correos import enviar_correo

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('roles', RolViewSet)
router.register('sensores', SensorViewSet)
router.register('lecturas', LecturaSensorViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # RUTAS DE APIS INDEPENDIENTES
    path('chat/', chatbot),
    path('chat_ia/', chatbot_ia),
    path('correo/', enviar_correo),
]
