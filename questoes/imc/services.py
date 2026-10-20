def calculo_imc(altura, peso):
    imc = peso / (altura * altura)

    if (imc < 18.5):
        return "Abaixo do peso"
    
    elif (imc <= 24.9):
        return "Peso normal"
    
    elif (imc <= 29.9):
        return "Sobrepeso"
    
    else:
        return "Obesidade"