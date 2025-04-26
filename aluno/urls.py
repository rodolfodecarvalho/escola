from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno, name="aluno"),
    path('cadastrar', views.cadastrar, name="cadastrar"),
]