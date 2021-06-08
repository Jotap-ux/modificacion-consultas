var btn = document.getElementById('btnEnviarConsulta');

function msgConsulta(){
    var nombre = document.getElementById('txtNombre').value;
    var correo = document.getElementById('txtCorreoConsulta').value;
    var comentario = document.getElementById('txtComentario').value;
    if(nombre.length>2 && correo.length>9 && comentario.length>9) {
        alert("Consulta Enviada!! =)");
    }else{
        Swal.fire({
            position: 'top-end',
            icon: 'error',
            title: 'Datos incorrectos! :(',
            showConfirmButton: false,
            timer: 1500
          })
    }
}

btn.addEventListener('click',msgConsulta,true);