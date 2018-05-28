from AppSena.models import *
from .serializer import *
from rest_framework import viewsets

#============== Tabla User De DJANGO ===========================
class user_viewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class =  user_serializer
#===============================================================
class permiso_viewset(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class =  permiso_serializer

class persona_viewset(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class =  persona_serializer

class permiso_persona_viewset(viewsets.ModelViewSet):
	queryset = Permiso_persona.objects.all()
	serializer_class =  permiso_persona_serializer

class rol_viewset(viewsets.ModelViewSet):
	queryset = Rol.objects.all()
	serializer_class =  rol_serializer

class rol_persona_viewset(viewsets.ModelViewSet):
	queryset = Rol_persona.objects.all()
	serializer_class =  rol_persona_serializer

class programa_viewset(viewsets.ModelViewSet):
	queryset = Programa.objects.all()
	serializer_class =  programa_serializer

class ficha_viewset(viewsets.ModelViewSet):
	queryset = Ficha.objects.all()
	serializer_class =  ficha_serializer

class persona_ficha_viewset(viewsets.ModelViewSet):
	queryset = Persona_ficha.objects.all()
	serializer_class =  persona_ficha_serializer
