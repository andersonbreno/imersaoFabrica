from logging import PlaceHolder
from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=80)
    sobre = models.CharField(max_length=200)
    conteudo = models.TextField()
    categoria = models.TextField()
    observacoes = models.TextField()
    email = models.EmailField()
    data_publicacao = models.DateField(auto_now_add=True)

    # mais duas tabelas/atributos aqui ... trazer do forms