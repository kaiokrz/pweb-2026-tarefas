from django.shortcuts import render
from datetime import date

def index(request):
    context = {'hoje':date.today().strftime('%d/%m/%Y')}
    return render(request, "index.html", context)