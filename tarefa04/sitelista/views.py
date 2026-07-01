from django.shortcuts import render
from datetime import date
from sitelista.models import Tarefa

tarefas = Tarefa.objects.all()
hoje = date.today()

def index(request):
    context = {'tarefas':tarefas,'hoje':hoje}
    return render(request, "index.html", context)