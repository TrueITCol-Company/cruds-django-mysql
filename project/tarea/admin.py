from django.contrib import admin
#importar modelo
from .models import Tarea, TipoTarea

#configuración administrador de modelo
@admin.register(Tarea)
class TareasAdmin(admin.ModelAdmin):
    """Tareas admin."""
    list_display = ('id', 'nombre', 'fecha', 'descripcion', 'finalizada')

@admin.register(TipoTarea)
class TipoTareasAdmin(admin.ModelAdmin):
    """Tipo Tareas admin."""
    list_display = ('id', 'nombre', 'descripcion')
