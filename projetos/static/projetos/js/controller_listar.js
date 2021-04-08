$(document).ready(function() {
    console.log( "ready!" );

    $("button[name='calcular']").on("click", function() {
      var valor = parseInt($(this).parent().find("input[name='valor']").val());
      var risco = parseInt($(this).parent().find("input[name='risco']").val());
      var investimento = parseInt($(this).parent().find("input[name='investimento']").val());
      var alerta = ($(this).parent().find(".alert"));

      if (valor > investimento) {
        alerta.show();
      } else {
        alerta.hide();
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
      }
    });
});
