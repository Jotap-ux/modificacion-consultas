from django.contrib import admin

# Importamos los modelos que queremos Administrar
from .models import TipoAtencion, Atencion, Galeria

# Clase para mostrar ciertas caracteristicas nuevas en el entorno administrable
class AtencionAdmin(admin.ModelAdmin):
    list_display = ["id","trabajador", "fecha", "publicado", "comentario"] # Lista de campos que se mostrarán 
    list_editable = ["trabajador", "publicado", "comentario"] # Lista de campos que podrán editarse directamente
    list_filter = ["id"] # Por que campos se hará un filtro 
    list_per_page = 5 # Páginador que agrupa 5 objetos por página
    search_fields = ["id","trabajador", "fecha" ] # Campos que se podrán buscar mediante palabras claves

class TipoAtencionAdmin(admin.ModelAdmin):
    list_display = ["id", "categoria", "imagen_categoria"]
    list_filter = ["id","categoria"]
    list_editable = ["categoria"]
    list_per_page = 8
    search_fields = ["id","categoria"]

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ["id_galeria","imagen_galeria","atencion"]
    list_filter = ["id_galeria"]
    list_per_page = 5
    search_fields = ["id_galeria","atencion"]

# Register your models here.
# Registramos y ya pueden ser utilizados en el entorno de administración
admin.site.register(TipoAtencion,TipoAtencionAdmin)
admin.site.register(Atencion,AtencionAdmin)
admin.site.register(Galeria,GaleriaAdmin)
