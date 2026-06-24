from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    prazo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    def atraso(self, data):
        if(self.prazo<data):
            return "Atrasado"