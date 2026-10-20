async function bloquearRecarregamento(event) {
    event.preventDefault();
    const formulario = event.target;

    const resposta = await fetch(formulario.action, {
        method: 'POST',
        body: new FormData(formulario)
    });
    
    const dados = await resposta.json();
    const classeCss = dados.classificacao.toLowerCase().replace(" ", "-");

    document.getElementById("area_resultado").innerHTML = `
        <div class="resposta_imc ${classeCss}">
            <p class="titulo_resultado"> <strong>Resultado do IMC:</strong> ${dados.imc} </p>
            <p class="descricao_resultado"> <strong>Classificação:</strong> ${dados.classificacao} </p>
        </div>
    `; 
    document.querySelector(".linha_separadora").style.display = "block"
    document.querySelector(".repetir_calculo").style.display = "block"
}