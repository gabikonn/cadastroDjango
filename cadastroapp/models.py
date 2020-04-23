from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    altura = models.CharField(max_length=5)
    dataNascimento = models.CharField(max_length=8)
# Create your models here.
