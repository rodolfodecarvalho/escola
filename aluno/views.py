from django.shortcuts import render

def aluno(request):
    return render(request, "aluno.html")

def cadastrar(request):
    return render(request, "cadastrar.html")