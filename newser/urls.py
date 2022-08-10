from  django.urls import path
from newser.views import Cursolist,DeleteCurso,CreateDocente,home,Userauth
urlpatterns = [
       path('',Cursolist.as_view(),name='homepage'),
       path('login',home),
       path('eliminarcurso/<int:id>',DeleteCurso),
       path('createdocente/',CreateDocente),
       path('Userauth/',Userauth),

]
