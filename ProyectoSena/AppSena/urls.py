from django.urls import path
from .views import *

# URLS
urlpatterns = [
#=======================INDEX=====================#
    path('', view_index, name = 'url_index'),
    path('index/', view_index, name = 'url_index'),
#=================================================#

#=======================FICHAS====================#
	path('lista_fichas/', view_lista_fichas, name = 'url_lista_fichas'),
	#AGREGAR FICHA
	path('agregar_ficha/', view_agregar_ficha, name = 'url_agregar_ficha'),

	path('agregar_persona_ficha/', view_agregar_persona_ficha, name = 'url_agregar_persona_ficha'),
	#EDITAR FICHA
	path('editar_ficha/<int:id_ficha>/', view_editar_ficha, name = 'url_editar_ficha'),
	#ELIMINAR FICHA
	path('eliminar_ficha/<int:id_ficha>/', view_eliminar_ficha, name = 'url_eliminar_ficha'),
#=================================================#

#======================PERMISOS===================#
	path('lista_permisos/', view_lista_permisos, name = 'url_lista_permisos'),
#=================================================#

#======================PERSONAS====================#
	
	#AGREGAR ADMINISTRADOR
	path('agregar_admin/', view_agregar_administrador, name="url_agregar_admin"),
	
	#LISTA INSTRUCTORES
	path('lista_instructores/',view_lista_instructores, name='url_lista_instructores'),
	#AGREGAR INSTRUCTOR
	path('agregar_instructor/',view_agregar_instructor, name='url_agregar_instructor'),
	#Editar INSTRUCTOR
	path('editar_instructor/<int:id_instructor>/', view_editar_instructor, name='url_editar_instructor'),
	#eliminar INSTRUCTOR
	path('eliminar_instructor/<int:id_instructor>/', view_eliminar_instructor, name='url_eliminar_instructor'),

	#LISTA VIGILANTES
	path('lista_vigilantes/', view_lista_vigilantes, name= 'url_lista_vigilantes'),
	#AGREGAR VIGILANTE
	path('agregar_vigilante/',view_agregar_vigilante, name='url_agregar_vigilante'),
	#EDITAR VIGILANATE
	path('editar_vigilante/<int:id_vigilante>/', view_editar_vigilante, name= 'url_editar_vigilante'),
	#ELIMINAR VIGILANTE
	path('eliminar_vigilante/<int:id_vigilante>/', view_eliminar_vigilante, name= 'url_eliminar_vigilante'),

	#ListA aprendiCES
	path('lista_aprendices/', view_lista_aprendices, name='url_lista_aprendices'),
	#Agregar aprendiz
	path('agregar_aprendiz/', view_agregar_aprendiz, name = 'url_agregar_aprendiz'),
	#Editar Aprendiz
	path('editar_aprendiz/<int:id_aprendiz>/', view_editar_aprendiz, name='url_editar_aprendiz'),
	#eliminar Aprendiz
	path('eliminar_aprendiz/<int:id_aprendiz>/', view_eliminar_aprendiz, name='url_eliminar_aprendiz'),
	#Cargar Excel
	path('agregar_aprendiz_excel/', view_agregar_aprendiz_excel, name='url_agregar_aprendiz_excel'),
	#REGISTROS_EXCEL
	path('registros_excel/', cargar_excel, name = 'url_registros_excel'),
#=================================================#

#====================PROGRAMAS====================#
	path('lista_programas', view_lista_programas, name = 'url_lista_programas'),
	#AGREGAR PROGRAMA 
	path('agregar_programa/', view_agregar_programa, name='url_agregar_programa'),
	#EDITAR PROGRAMA 
	path('editar_programa/<int:id_programa>/', view_editar_programa, name='url_editar_programa'),
	#ELIMINAR PROGRAMA 
	path('eliminar_programa/<int:id_programa>/', view_eliminar_programa, name='url_eliminar_programa'),
#=================================================#

#=====================USUARIOS====================#
	path('usuario/index/', view_usuario, name = 'url_usuarios'),
#=================================================#

#=====================ROLES====================#
	#Listar rol
	path('lista_roles', view_lista_roles, name = 'url_lista_roles'),
	#Agregar rol
	path('agregar_rol/',view_agregar_rol, name='url_agregar_rol'),
	#Editar rol
	path('editar_rol/<int:id_rol>/',view_editar_rol, name='url_editar_rol'),
	#Eliminar rol
	path('eliminar_rol/<int:id_rol>/',view_eliminar_rol, name='url_eliminar_rol'),


#=====================LOGIN====================#
	path('login/', view_login, name = 'url_login'),
	#LOGOUT
	path('logout/', view_logout, name = 'url_logout'),
#===============================================#

]
