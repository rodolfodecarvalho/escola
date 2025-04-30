from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno, name="aluno"),
    path("excluir/<int:id>", views.exluir, name="exluir"),
    path("atualizar/<int:id>", views.atualizar, name="atualizar"),
    path('cadastro/', views.Cadastro.as_view(), name="cadastro")
]