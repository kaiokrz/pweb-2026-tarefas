from django.db import models


class Tarefas(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    prazo = models.CharField(max_length=100)
