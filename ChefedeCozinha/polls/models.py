from django.db import models

# Create your models here.

class Cardapio(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField
    receita_produto = models.CharField(max_length=200)


    def __str__(self):
        return self.nome_produto