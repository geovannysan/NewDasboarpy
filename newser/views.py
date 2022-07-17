from django.shortcuts import render
from .models import Curso
# Create your views here.

def home(request):
    userlista =Curso.objects.all()
    return render(request,'homepage.html',{"curso":userlista})


