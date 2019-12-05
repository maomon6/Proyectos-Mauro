from django.contrib import admin

# Importar cada una de las clases creadas en el archivo models.py

from.models import etnia
from.models import TipoDocu
from.models import EstadoCivil
from.models import TipoEstu
from.models import TipoLogr

# Agregar la clase Model>>ModelAdmin para modificar la vista a cada uno de los modelos importados
class EtniaModelAdmin(admin.ModelAdmin):

    # Indicar que columnas queremos ver (para este caso solo mostramos el nombre ya que no hay otras)
    list_display = ["NombEtni"]
    # Indicar en qué columna hacer click para editar
    list_display_links = ["NombEtni"] 
    # Agregar una barra de búsqueda
    search_fields = ["NombEtni"]
    # Agregar un filtro
    list_filter = ["NombEtni"]
    # Indicar desde dónde se obtienen esos parámetros
    class Meta:
        model = etnia

# Register your models here.
admin.site.register(etnia)
admin.site.register(TipoDocu)
admin.site.register(EstadoCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)