from django.http import JsonResponse
from django.shortcuts import render
from . import services

def calcular_imc(request):
    if (request.method == 'GET'):
        return render(request, 'imc/index.html')

    elif (request.method == 'POST'):
        altura = float(request.POST.get('altura'))
        peso = float(request.POST.get('peso'))
        classificacao = services.calculo_imc(altura, peso)
        valor_imc = peso / (altura * altura)

        contexto = {
            'peso': peso,
            'altura': altura,
        }

        return JsonResponse ({
            'imc': f"{valor_imc:.2f}",
            'classificacao': classificacao
        })