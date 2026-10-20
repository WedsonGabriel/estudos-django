from django.shortcuts import render
from .models import Despesa

def pagina_controleDespesas(request):
    if (request.method == "GET"):
        return render(request, 'controleDespesas/index.html')

    elif (request.method == "POST"):
        descricao_req = request.POST.get('descricao')
        categoria_req = request.POST.get('categoria')
        valor_req = request.POST.get('valor')
        data_req = request.POST.get('data')
        pago_req = 'pago' in request.POST

        Despesa.objects.create(
            descricao = descricao_req,
            categoria = categoria_req,
            valor = valor_req,
            data = data_req,
            pago = pago_req,
        )

        lista_despesas = Despesa.objects.all()
        return render(request, "controleDespesas/partials/table.html", {'despesas':lista_despesas})

def mostrar_tabela(request):
    lista_despesas = Despesa.objects.all()
    return render(request, "controleDespesas/partials/table.html", {'despesas':lista_despesas})