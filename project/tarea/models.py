from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    fecha = models.DateField("fecha", auto_now=False, auto_now_add=False)
    descripcion = models.CharField("descripcion", max_length=50)
    finalizada = models.BooleanField("finalizada")
    created_at = models.DateTimeField("create_at", auto_now_add=True)
    updated_at = models.DateTimeField("update_at", auto_now=True) 

    class Meta:
        db_table = 'tareas'

class TipoTarea(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.CharField("descripcion", max_length=50)
    created_at = models.DateTimeField("create_at", auto_now_add=True)
    updated_at = models.DateTimeField("update_at", auto_now=True) 

    class Meta:
        db_table = 'tipotareas'