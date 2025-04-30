from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from aluno.forms import AlunoForm
from aluno.models import Aluno

def aluno(request):
    return render(request, "aluno.html")

def exluir(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    aluno.delete()

    return redirect("cadastro")

def atualizar(request, id):
    aluno = get_object_or_404(Aluno, id=id)


    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')

    aluno.nome = nome
    aluno.email = email
    aluno.telefone = telefone

    aluno.save()

    return redirect('cadastro')

class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = AlunoForm

    def get(self, request):
        alunos = Aluno.objects.all()

        return render(request, self.template_name, {'form' : self.form_class(), 'alunos': alunos})
    
    def post(self, request):
        form = self.form_class(request.POST)
        alunos = Aluno.objects.all()

        if form.is_valid():
            obj = form.save(commit=False)
            obj.active = True

            obj.save()

            return render(request, self.template_name, {'form' : self.form_class(), 'alunos': alunos})
        
        return render(request, self.template_name, {'form' : form, 'alunos': alunos})