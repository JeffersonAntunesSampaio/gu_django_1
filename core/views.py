from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):
    print(f'Metodo: {request.method}')
    print(f'Cabeçalho: {request.headers}')
    print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'logado': teste,
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):

    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)

    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(
        content=template.render(),
        content_type='text/html; charset=utf8',
        status=404
    )


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(
        content=template.render(),
        content_type='text/html; charset=utf8',
        status=500
    )
