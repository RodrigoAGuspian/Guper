from django.urls import path, include
from rest_framework import routers
from AppSena.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'user', user_viewset)
router.register(r'permiso', permiso_viewset)
router.register(r'persona', persona_viewset)
router.register(r'permiso_persona', permiso_persona_viewset)
router.register(r'rol', rol_viewset)
router.register(r'rol_persona', rol_persona_viewset)
router.register(r'programa', programa_viewset)
router.register(r'ficha', ficha_viewset)
router.register(r'persona_ficha', persona_ficha_viewset)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]