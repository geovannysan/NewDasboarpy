from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso
# Create your views here.

def home(request):
    userlista =Curso.objects.all()
    return render(request,'homepage.html',{"curso":userlista})

class Cursolist(ListView):
    model = Curso
    template_name ='homepage.html'
    def get_queryset(self):
        return Curso.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        contex=super().get_context_data(**kwargs)

        return contex


