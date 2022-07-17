from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre= models.CharField(max_length=100)
    creditos=models.PositiveSmallIntegerField()
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
