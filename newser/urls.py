from django.views import debug
from  django.urls import path
from newser.views import Cursolist,DeleteCurso,CreateDocente,LoginViewst,Logoutredir,FoginViewst
urlpatterns = [
       path('', debug.default_urlconf),
       path('home',Cursolist.as_view(),name='homepage'),
       path('login',FoginViewst.as_view(),name='login'),
       path('eliminarcurso/<int:id>',DeleteCurso),
       path('createdocente/',CreateDocente),
       path('logout/',Logoutredir.as_view(),name='logout')
      

]
