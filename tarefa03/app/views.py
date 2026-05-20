from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")

def usuarios(request):
    users = [
        {"nome": "cassiano", "idade": 18, "cidade": "São Tomé", "matricula": "333"},
        {"nome": "alvaros", "idade": 15, "cidade": "São Paulo do Potengi", "matricula": "123"},
        {"nome": "Gustavo", "idade": 18, "cidade": "Bom Jesus", "matricula": "321"},
        {"nome": "Julio", "idade": 25, "cidade": "Boa Saúde", "matricula": "124"},
        {"nome": "hugo", "idade": 18, "cidade": "Elói de Souza", "matricula": "008"},
    ]

    context = {
        "usuarios":users
    }

    return render(request, "app/usuarios.html", context)