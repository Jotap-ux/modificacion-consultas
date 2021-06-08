    fetch("https://mindicador.cl/api/dolar").then(
        function (response) {
            if(response.status!=200){
                alert("No se pudo conectar al servicio.");
                return;
            }
            // Recuperar datos de la respuesta
            response.json().then(function(data){
                var dolar = data.serie[0].valor;
                var etiqueta = document.getElementById("txtDolar").innerHTML = "Valor Dólar : $" + dolar;
            })
        }
    )