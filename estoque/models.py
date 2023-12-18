from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    codigo_produto = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.FloatField()
