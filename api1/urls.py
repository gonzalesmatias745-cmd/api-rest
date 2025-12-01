from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RolViewSet, SensorViewSet, LecturaSensorViewSet

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('roles', RolViewSet)
router.register('sensores', SensorViewSet)
router.register('lecturas', LecturaSensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
