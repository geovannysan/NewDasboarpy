from django.conf.global_settings import MEDIA_URL,STATIC_URL
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Docente(models.Model):
    nombre= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    fecha_nacimiento= models.DateField()
    def nombre_completo(self):
        return "{}{},{}".format(self.lastname, self.firstname,self.nombre)
    def __str__(self):
        return self.nombre_completo()
    class  Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table='docente'
        ordering=['nombre','-lastname']
class Curso(models.Model):
    nombre= models.CharField(max_length=100)
    creditos=models.PositiveSmallIntegerField()
    email=models.CharField(max_length=100)
    docente= models.ForeignKey(Docente ,null=False ,blank=True ,on_delete = models.CASCADE)
    def nombres_completos(self):
        return "{}{},{}".format(self.nombre, self.creditos,self.email)
    def __str__(self):
        return self.nombres_completos()
    class Meta:
        verbose_name= 'Curso'
        verbose_name_plural= 'Cursos'
        db_table= 'curso'
        ordering=['nombre','-creditos']

class Usuarios(AbstractUser):
    imgen = models.ImageField(upload_to='user/%y/%m/%d',null=True,blank=True)
    def get_image(self):
        if self.imgen:
            return '{}{}'.format_map(MEDIA_URL,self.imgen)
        return '{}{}'.format(STATIC_URL,'static/gps.png')
