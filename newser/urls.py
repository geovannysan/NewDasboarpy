from  django.urls import path
from newser.views import Cursolist
urlpatterns = [
       path('',Cursolist.as_view(),name='homepage'),
]
