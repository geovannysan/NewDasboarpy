from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Curso,Docente
# Create your views here.

def home(request):
    return render(request,'login.html')

class Cursolist(ListView):
    model = Docente
    template_name ='homepage.html'
    def get_queryset(self):
        return Docente.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex["titulo"]="Docentes"
        
        return contex
def DeleteCurso(request,id):
    print(request,id)
    prof = Docente.objects.get(id=id)
    prof.delete()
    return  redirect('/')

def CreateDocente(request):
    nom = request.POST['names']
    seg = request.POST['se']
    ed = request.POST['validationCustomUsername']
    fe = request.POST['validationCustom03']
    curso = Docente.objects.create(nombre=nom,lastname=seg,firstname=ed,fecha_nacimiento=fe)
    return redirect('/')
def  Userauth(request):
    usename = request.POST['username']
    password = request.POST['password']
    #user = authenticate(request,username=username,password=password)
    #if username is not None:
     #   login(request,user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('/')
    #else:
     #   print("no existe")
    
   



