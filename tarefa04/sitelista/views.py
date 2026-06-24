from django.shortcuts import render
from datetime import date
from sitelista.models import Tarefa

def index(request):
    context = {'tarefas':Tarefa.objects.all(),'hoje':date.today().strftime('%d/%m/%Y')}
    return render(request, "index.html", context)