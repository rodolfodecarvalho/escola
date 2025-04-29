from django import forms

from aluno.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'telefone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.setdefault('class', 'form-control')

        self.fields['telefone'].widget.attrs.update({'data-mask': '(00) 00000-0000'})
