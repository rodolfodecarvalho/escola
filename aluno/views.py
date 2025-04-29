from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from aluno.forms import AlunoForm

def aluno(request):
    return render(request, "aluno.html")


class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = AlunoForm

    def get(self, request):
        return render(request, self.template_name, {'form' : self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.active = True

            obj.save()

            return HttpResponse('Cadastro realizado com sucesso')
        
        return render(request, self.template_name, {'form' : form})