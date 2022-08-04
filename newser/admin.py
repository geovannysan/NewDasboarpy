from django.contrib import admin
from  .models import Curso,Docente
# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','creditos')
    list_per_page = 5

admin.site.register(Docente)

