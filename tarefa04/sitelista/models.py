from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(verbose_name="Concluído")
    prazo = models.DateField()
    def __str__(self):
        return self.nome
    
    def atraso(self, data):
        if(self.prazo<data):
            return "Atrasado"