from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    altura = models.CharField(max_length=5)
    dataNascimento = models.CharField(max_length=8)

class novoCadastro(models.Model):
    nome = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    dataNasc= models.DateTimeField()

    def __str__(self):
        return self.nome
# Create your models here.
