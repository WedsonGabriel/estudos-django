from django.shortcuts import render
from .models import Livro

def pagina_catalogoLivros(request):
    if (request.method == "GET"):
        return render(request, 'catalogoLivros/index.html')

    elif (request.method == "POST"):
        titulo_req = request.POST.get('titulo')
        autor_req = request.POST.get('autor')
        ano_req = request.POST.get('ano')
        genero_req = request.POST.get('genero')
        status_req = request.POST.get('status') == 'disponivel'

        Livro.objects.create(
            titulo = titulo_req,
            autor = autor_req,
            ano = ano_req,
            genero = genero_req,
            status = status_req,
        )

        livros_salvos = Livro.objects.all()
        return render(request, 'catalogoLivros/partials/table.html', {'livros':livros_salvos})

def buscar_tabela(request):
    livros_salvos = Livro.objects.all()
    return render(request, 'catalogoLivros/partials/table.html', {'livros': livros_salvos})