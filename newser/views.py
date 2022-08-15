from django.contrib.auth import  login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, RedirectView
from .models import Curso,Docente
# Create your views here.

class LoginViewst(LoginView):
    template_name ='login.html'
    success_url = reverse_lazy('/home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        if form.is_valid():
            login(self.request, form.get_user())
            return HttpResponseRedirect(self.success_url)
    def form_invalid(self, form,**kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx['form'] = form
        return self.render_to_response(ctx)
        
    def get_context_data(self,**kwargs):
        contex = super().get_context_data(**kwargs)
        contex['titulo']='Iniciar'
        return contex
class FoginViewst(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('/home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['titulo'] = 'Iniciar'
        return contex
class Logoutredir(RedirectView):
    pattern_name = 'login'
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
class Cursolist(ListView):
    model = Docente
    template_name ='homepage.html'
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated :
            return redirect('/login')        
        return super().dispatch(request,*args,**kwargs)
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
    return  redirect('/home')
def CreateDocente(request):
    nom = request.POST['names']
    seg = request.POST['se']
    ed = request.POST['validationCustomUsername']
    fe = request.POST['validationCustom03']
    curso = Docente.objects.create(nombre=nom,lastname=seg,firstname=ed,fecha_nacimiento=fe)
    return redirect('/home')

   



