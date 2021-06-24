from tallerMecanico.models import Atencion, TipoAtencion
from rest_framework import serializers

#crear una clase que permita serializar una tabla  y sus campos

class AtencionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = ["id","diagnostico","fecha","trabajador"]

class TipoAtencionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoAtencion
        fields = ["id","categoria","imagen_categoria"]

