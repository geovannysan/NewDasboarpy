from  django.urls import path
from newser.views import Cursolist,DeleteCurso,CreateDocente
urlpatterns = [
       path('',Cursolist.as_view(),name='homepage'),
       path('eliminarcurso/<int:id>',DeleteCurso),
       path('createdocente/',CreateDocente)
]
