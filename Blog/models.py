from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = RichTextField()
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    equipo = models.CharField(max_length=40, default="Team Involved")
    jugador_actual = models.CharField(max_length=40, default="Player/s Involved")