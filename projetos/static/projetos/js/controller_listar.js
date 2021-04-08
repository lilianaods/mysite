$(document).ready(function() {
    console.log( "ready!" );

    $("button[name='calcular']").on("click", function() {
      var risco = parseInt($(this).parent().find("input[name='risco']").val());
      var investimento = parseFloat($(this).parent().find("input[name='investimento']").val().replace(',', '.'));

      var retorno;

      var aux = $(this).parent().find('span[id^="retornoInvestimento"]');

      switch(risco) {
        case 0:
           retorno = investimento * 0.05;
           break;
        case 1:
           retorno = investimento * 0.1;
           break;
        case 2:
           retorno = investimento * 0.2;
           break;
        default:
          // code block
      }

      aux.text(String(retorno.toFixed(2)).replace('.', ','));
    });
});
