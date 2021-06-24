from django.db.models.query import QuerySet
from django.shortcuts import render
#Páginas web prediseñadas de REST_FRAMEWORK
from rest_framework import generics
from tallerMecanico.models import Atencion, TipoAtencion
from .serializers import AtencionSerializers, TipoAtencionSerializers
from api import serializers


# Create your views here.

#Clase que va a mostrar un conjunto de datos

class AtencionViewSet(generics.ListAPIView):
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializers

class TipoAtencionViewSet(generics.ListAPIView):
    queryset = TipoAtencion.objects.all()
    serializer_class = TipoAtencionSerializers

#ViewSet con parametro
class AtencionBuscarViewSet(generics.ListAPIView):
    serializer_class = AtencionSerializers
    def get_queryset(self):
        id_atencion = self.kwargs['id']
        return Atencion.objects.filter(id=id_atencion)

class TipoAtencionBuscarViewSet(generics.ListAPIView):
    serializer_class = TipoAtencionSerializers
    def get_queryset(self):
        id_categoria = self.kwargs['id']
        return TipoAtencion.objects.filter(id=id_categoria)
