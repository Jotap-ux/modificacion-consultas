from django.contrib import admin
from django.urls import path, include 
from .views import cerrarSesion, eliminarAtencion, filtrar, index, pagModificarAtencion, mostrarAtencion, servicios, ubicacion, consulta, registrarse, galeria , iniciarSesion, detalleAtencion, mostrarAtencion, administrarAtencion, actualizar, insertarImagen, mostrarconsulta, listarConsulta, eliminarConsulta
# De las views importamos los métodos para renderizar las páginas

urlpatterns = [
    path('',index,name='INDEX'),
    path('ubicacion/',ubicacion, name='UBICACION'),
    path('registrarse/',registrarse,name='REGISTRARSE'),
    path('consulta/',consulta,name='CONSULTA'),
    path('galeria/',galeria, name='GALERIA'),
    path('logout/',cerrarSesion,name = 'LOGOUT'),
    path('login/',iniciarSesion,name = 'LOGIN'),
    path('atenciones/', detalleAtencion, name = 'ATENCION'),
    path('atencion/<id>/',mostrarAtencion, name = 'FICHA' ), #Le entregamos una ID
    path('filtro/',filtrar,name='FILTRO'),
    path('adminAtencion/',administrarAtencion,name = 'ADMIN_ATENCION'),
    path('pagModificarAtencion/<id>/',pagModificarAtencion, name = 'MODIFICAR_ATENCION'),
    path('actualizar/',actualizar,name = "ACTUALIZAR"), 
    path('eliminar/<id>/', eliminarAtencion, name = "ELIMINAR"),
    path('insertarImagen/',insertarImagen,name = 'INSERTAR_IMG'),
    path('servicios/',servicios,name='SERVICIOS'), # Con API REST
    path('mostrarconsulta/',mostrarconsulta,name='MOSTRARC'),
    path('listarconsulta/',listarConsulta, name='LISTA_CON'),
    path('eliminarconsulta/<id>/',eliminarConsulta, name='ELIMINAR_CON')
]