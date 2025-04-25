from django.shortcuts import render

def aluno(request):
    return render(request, "aluno.html")