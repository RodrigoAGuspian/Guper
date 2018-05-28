from django import forms
from django.contrib.auth.models import User
from .models import *
from datetime import datetime, date


class agregar_programa_form(forms.ModelForm):
	class Meta:
		model = Programa
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput(attrs ={'placeholder': 'alguien@misena.edu.co'}))
	contraseña = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'placeholder': 'PASSWORD'}))
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

		labels={
			'persona':'aprendiz',
		}

##---------------------------------------------------------##
#        REGISTRAR VIGILANTE, APRENDIZ, INSTRUCTOR          #

class agregar_persona_form(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude=('usuario',)
#agregar user a APRENDEIZ, INSTRUCTOR y ADMIN
class agregar_user_form(forms.ModelForm):
	class Meta:
		model= User
		fields=['email']

		labels={
			'email':'Correo Electronico',
		}

		widgets = {
			'email': forms.TextInput(attrs ={'placeholder': 'alguien@misena.edu.co'})
		}

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'misena.edu.co' in email:
			raise forms.ValidationError('Debes ingresar un correo misena. alguien@misena.edu.co')

		return email

class agregar_user_vigilante_form(forms.ModelForm): #agregar user a VIGILANTE
	class Meta:
		model= User
		fields=['username']

		labels={
			'username':'Correo Electronico',
		}

class editar_user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','password']

		widgets = {
			'password' : forms.PasswordInput(render_value=False),
		}


##-------------------------------------------------------------##

class elegir_ficha_form(forms.ModelForm):
	class Meta:
		model = Persona_ficha
		fields = ['ficha']

class elegir_rol_form(forms.ModelForm):
	class Meta:
		model = Rol_persona
		fields = ['rol']

class cargar_excel_form(forms.Form):
	excel =forms.FileField()

#============================================
	