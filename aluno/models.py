from django.db import models
from django.core.validators import RegexValidator
from dataclasses import dataclass


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15,
                                blank=True,
                                validators=[RegexValidator(regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$', 
                                                                      message='Número de telefone inválido. Use o formato (99) 99999-9999.')],
                                                                      help_text='Use o formato (99) 99999-9999.')
    active = models.BooleanField(db_default=True)
