from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno, name="aluno"),
    path('cadastro/', views.Cadastro.as_view(), name="cadastro")
]