
function validacion() {

    var password = validaConfirmacionPass();

    if (password==false) {
        return false;
    }
    alert('Se ha registrado con exito :)');
     
	return true;
}



function validaConfirmacionPass(params) {
    var pass = document.getElementById('txtContraseña').value;
    var pass2 = document.getElementById('txtConfirmar').value;

    if (pass == pass2) {
        return true;
    }
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'La contraseña debe ser la misma!!'
      })
    return false;
}

function validaUsuario(mensaje){
    valida = false;
    if(mensaje.equals("0")){
        valida = true;
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El Usuario ya existe!!'
            
          })
        return valida;
    }

    return valida;
}

//-----------------------------------------------------------------------



function valida() {

    resp = validaFecha();
    if ( resp == false) {
        return false;
    }
    
    return true;
}

function validaFecha() {
    var fechaControl = document.getElementById('fecha-atencion').value;
    var fechaSistema = new Date();
    /////////////////// 
    var ano = fechaControl.slice(0,4);
    var mes = fechaControl.slice(5,7);
    var dia = fechaControl.slice(8,10);
    /*alert('Año:' + ano);
    alert('Mes:' + mes);
    alert('Dia:' + dia);*/
    var fechaDelControl = new Date(ano,(mes-1),dia);
    //alert(fechaDelControl);
    if ( fechaDelControl > fechaSistema ) {
        //alert('fecha de nacimiento incorrecta');
        //Swal.fire('fecha de nacimiento incorrecta');
        alert('fecha incorrecta, es del futuro niño troll xd');
        return false;
    }
    
}




