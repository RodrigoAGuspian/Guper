from rest_framework import serializers
from AppSena.models import *
#============== Tabla User De DJANGO ===========================
from django.contrib.auth.models import User

class user_serializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('url','username','password')
#================================================================

#======================= PERMISO ================================
class permiso_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Permiso
		fields = ('url','motivo','solicitoPermisoPor','permisoPorHora','permisoPorDias','horaSalida','fecha',)
#================================================================

#======================= PERSONA ================================
class persona_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Persona
		fields = ('url','documentoIdentidad','primerNombre','segundoNombre','primerApellido','segundoApellido','contacto','usuario',)
#=================================================================

#======================= PERMISO_PERSONA =========================
class permiso_persona_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Permiso_persona
		fields = ('url','estado','instructor','vigilante','permiso','persona',)
#==================================================================

#=========================== ROL ==================================
class rol_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Rol
		fields = ('url','rol',)
#===================================================================

#=========================== ROL_PERSONA ===========================
class rol_persona_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Rol_persona
		fields = ('url','rol','persona',)
#=================================================================

#=========================== PROGRAMA ============================
class programa_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Programa
		fields = ('url','nombre','codigoPrograma',)
#==================================================================

#=========================== FICHA ================================
class ficha_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Ficha
		fields = ('url','numeroFicha','jornada','ambiente','lider','fechaFinEtapaLectiva','programa',)
#==================================================================

#=========================== PERSONA_FICHA ========================
class persona_ficha_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Persona_ficha
		fields = ('url','persona','ficha','programa',)
#==================================================================