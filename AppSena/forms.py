from django import forms
from django.contrib.auth.models import User
from .models import *

class agregar_programa_form(forms.ModelForm):
	class Meta:
		model = Programa
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput(attrs ={'placeholder': 'USUARIO'}))
	contraseña = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'CONTRASEÑA'}))

class agregar_rol_form(forms.ModelForm):
	class Meta:
		model= Rol 
		fields= '__all__'

class agregar_ficha_form(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'

class agregar_persona_ficha_form(forms.ModelForm):
	class Meta:
		model = Persona_ficha
		fields = '__all__'

##-------------------------------------##
#          Registrar vigilante          #

class agregar_persona_form(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude=('usuario','documentoIdentidad',)

class agregar_user_form(forms.ModelForm):
	class Meta:
		model= User
		fields=['username','password',]

		labels={
			'username':'Correo Electronico',
			'password':'Documento'
		}


class editar_user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email']


##-------------------------------------##

class cargar_excel_form(forms.Form):
	excel =forms.FileField()

		