from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

# Registramos atenciones
class TipoAtencion(models.Model):
    categoria = models.CharField(max_length = 50)
    imagen_categoria = models.ImageField(upload_to = 'categorias')

    def __str__(self):
        return self.categoria

class Atencion(models.Model):
    diagnostico = models.TextField(max_length = 40)
    fecha = models.DateField(null=True)
    imagen = models.ImageField(upload_to = 'atenciones') #Nulo por ahora
    materiales = models.TextField(max_length = 40)
    id_atencion = models.ForeignKey(TipoAtencion, on_delete = CASCADE)
    publicado = models.BooleanField(default = False)
    comentario = models.CharField(max_length = 40, default = "N/A")
    trabajador = models.CharField(max_length = 30)

    def __str__(self):
        return self.trabajador

class Galeria(models.Model):
    id_galeria = models.AutoField(primary_key = True)
    imagen_galeria = models.ImageField( upload_to = 'galeria', null = True)
    atencion = models.ForeignKey(Atencion, on_delete = CASCADE)

    def __str__(self):
        return "ID : " + str(self.id_galeria)

class FormularioConsulta(models.Model):
    categoria = models.CharField(max_length = 15)
    comentario = models.TextField(max_length = 40)

    def __str__(self):
        return self.categoria


