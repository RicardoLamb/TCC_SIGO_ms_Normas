from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Normas(models.Model):
    class NormasObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='ativo')
    
    options = (('ativo', 'Ativo')), ('inativo', 'Inativo'),

    sigla = models.CharField(max_length=10, null=True)
    codigo = models.CharField(max_length=20, null=True)
    vigencia = models.CharField(max_length=20, null=True)
    fonte = models.TextField(null=True)
    area = models.TextField(null=True)
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    consequencias = models.TextField(null=True)
    acoes = models.TextField(null=True)
    usocorreto = models.TextField(null=True)
    descarte = models.TextField(null=True)
    riscos = models.TextField(null=True)
    status = models.CharField(max_length=10, choices=options, default='ativo')
    objects = models.Manager()
    normasobjects = NormasObjects()

    # Area = ambiental, industrial, saude, etc (vem do SOA) --desabilitado OK
    # Ações = OK
    # Uso Correto = OK
    # Descarte = OK
    # Riscos = OK
    # Consequencias = OK
    # Fonte = (vem do SOA é um link) --desabilitado OK
    # Vigência = (vem do SOA) --desabilitado OK
    # Titulo = OK
    # Descrição = OK    
    # Sigla = (vem do SOA) --selecionavel OK
    # Codigo = (vem do SOA) -- selecionavel OK

class Meta:
    ordering = ('-ativo',)

def __str__(self):
    return self.titulo