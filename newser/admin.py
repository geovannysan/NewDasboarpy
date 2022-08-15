from django.contrib import admin
from  .models import Curso,Docente
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios

admin.site.register(Usuarios)
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','creditos')
    list_per_page = 5

