from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print(request.method)
    print(request.GET.get('nome'))
    print(f"Bem vindo {request.META['HTTP_USER_AGENT']}")
    return render(request, "index.html")

def outra(request):
    return render(request, "outra.html")

def terceira(request):
    return redirect('outra')