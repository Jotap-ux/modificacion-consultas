from django.shortcuts import render, redirect

# Desde acá llamamos a los datos del Modelo
from .models import TipoAtencion, Atencion

# Importar el Modelo de Usuarios (User)
from django.contrib.auth.models import Group, User
#Importar librerias de validación
from django.contrib.auth import authenticate,logout,login
# importar libreria de decoradores que permite evitar el ingreso a páginas  restringidas
from django.contrib.auth.decorators import login_required, permission_required #Decoradores para restringuir acceso a las páginas
#Usamos as para ponerle un alias a una importación

# Create your views here.

# Acá creamos los métodos que renderizan las páginas y serán importamos en las urls

def index(request):
    #Mostramos las últimas 5 atenciones ordenadas por fecha
    listaAtenciones = Atencion.objects.filter(publicado = True).order_by('fecha')[:4]
    datos = {"atenciones":listaAtenciones}
    return render(request,'core/index.html',datos)

def servicios(request):
    listaServicios = TipoAtencion.objects.all()
    datos = {"lista":listaServicios}
    return render(request,'core/servicios.html',datos)

def ubicacion(request):
    return render(request, 'core/ubicacion.html')

def consulta(request):
    return render(request, 'core/consulta.html')

# PUBLICADO TRUE
def galeria(request):
    lista = Atencion.objects.filter (publicado = True)
    datos = {"listaAtenciones":lista}
    return render(request,'core/galeria.html',datos)

#Método para login
def iniciarSesion(request):
    if request.POST:
        usuario = request.POST.get("txtCorreo")
        password = request.POST.get("txtPass")
        us = authenticate(request,username = usuario, password = password)
        if us is not None and  us.is_active:
            #Cargamos al usuario en todas las páginas
            login(request,us)
            return render(request,"core/index.html")
        else:
            contexto = {"mensaje":"Correo electrónico o contraseña no válidos"}
            return render(request,'core/index.html',contexto)
    return render(request,'core/index.html')

def cerrarSesion(request):
    #Me cierra la sesión del usuario logeado en ese momento
    logout(request)
    return render(request,'core/index.html')

def registrarse(request):
    # En formato JSON
    # Si el request realiza un evento POST
    contexto = {"mensaje":""}
    if request.POST:
        # Guardamos en estas variables si el usuario envia por POST el formulario
        nom = request.POST.get("txtNombre")
        ape = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        passw = request.POST.get("txtContraseña")
        #No podemos poner directamente el ID como clave foránea
        #Trabajamos con Entidades
        #Porque usamos un ENTITY FRAMEWORK
        #Recuperamos el registro 
        # usu = Usuario.objects.create (email = correo, contrasenia = passw, id_tipo = obj_tipo) EN 1 Línea inserta los datos *TIP
        try:
            #Buscará ese nombre de usuario en la tabla User
            #Si no lo encuentra entrará en el bloque exception
            usu = User.objects.get(username = correo)
            contexto = {"mensaje":"El Usuario ya se encuentra registrado!!"}
            return render(request,'core/registrarse.html',contexto)
        except:
            #Al no encontrar usuario registrado se creará una instancia de User
            #Se le entregarán los atributos enviados desde el formulario
            #se guardará en la bd y luego iniciará sesión una vez registrado
            usu = User()
            usu.first_name = nom
            usu.last_name = ape
            usu.username = correo
            usu.email = correo
            usu.set_password(passw)
            usu.save()
            us = authenticate(request,username = correo,password = passw)
            login(request,us)
            contexto = {"mensaje":"Guardó el USUARIO CORRECTAMENTE"}
            return render(request,'core/index.html', contexto)

    return render(request,'core/registrarse.html')

@login_required(login_url='/login/') #Necesita estar logeado para subir atenciones
@permission_required('tallerMecanico.add_atencion',login_url='/login/')
def detalleAtencion(request):
    categorias = TipoAtencion.objects.all()
    nombre_trabajor = request.user.first_name + " " + request.user.last_name
    mensaje = "NOTHING"
    if request.POST:
        diag = request.POST.get("txtDiagnostico")
        fech = request.POST.get("txtFecha")
        img = request.FILES.get("txtImagen")
        mate = request.POST.get("txtMateriales")
        tipo = request.POST.get("cboCategoria")
        obj_tipo = TipoAtencion.objects.get(categoria = tipo)

        a = Atencion(
            diagnostico = diag,
            fecha = fech,
            imagen = img,
            materiales = mate,
            id_atencion = obj_tipo,
            trabajador = nombre_trabajor,
            publicado = False
        )
        a.save()
        mensaje = "GUARDADO"
    datos = {"categorias":categorias, "mensaje":mensaje}
        ### REVISARRR!!!!
        
    return render(request,'core/detalletrabajo-ingresar.html',datos)

#Método que nos muestra los datos de una atención
def mostrarAtencion(request,id):
    #Busco la atención por su ID y la guardo
    #luego entrego esa información en formato JSON a la página
    atencion = Atencion.objects.get(id = id)
    datos = {"atencion":atencion}
    return render(request,'core/fichaAtencion.html', datos)

# CAMBIAR LOS FALSE POR TRUE DESPUES
# Filtrar por Categoria - Mecanico y Palabras claves!
def filtrar(request):
    #Guardamos todas las atenciones si no se encuentra la que se busca
    atenciones = Atencion.objects.filter (publicado = False)
    datos = {"listaAtenciones":atenciones}
    if request.POST:
        texto = request.POST.get("filtro-busqueda")
        texto = texto.strip() # Quitamos los espacios en blanco del inicio
        if texto != "":
            try:
                categoria = TipoAtencion.objects.get(categoria = texto.upper())
                # Filtramos las atenciones que coincidan con la categoria ingresada
                atenciones = atenciones.filter(id_atencion = categoria)
                cantidad = atenciones.count()
                # En caso de que no se encuentre mostrar todas las atenciones
                datos = {"listaAtenciones":atenciones,"mensaje":"Filtrado por Categorias","cantidad":"Se encontraron " + str(cantidad) + " resultados"}
                return render(request,'core/galeria.html', datos)
            except:     
                atenciones = atenciones.filter(trabajador = texto.title()) # la variable texto sea igual al nombre del mécanico
                cantidad = atenciones.count()
                datos = {"listaAtenciones":atenciones,"mensaje":"Filtrado por Mecánicos","cantidad":"Se encontraron " + str(cantidad) + " resultados"}
                if cantidad == 0:
                    # Palabras claves diagnostico en diagnostico
                    atenciones = Atencion.objects.filter(diagnostico__contains = texto).filter(publicado =  False)
                    cantidad = atenciones.count()
                    datos = {"listaAtenciones":atenciones, "mensaje":"Filtrado por palabras claves", "cantidad":"Se encontraron " + str(cantidad) + " resultados"}
                    if cantidad == 0:
                        atenciones = Atencion.objects.all
                        datos = {"listaAtenciones":atenciones}
                        return render(request,'core/galeria.html', datos)
                    else:
                        return render(request,'core/galeria.html', datos)

    return render(request,'core/galeria.html', datos)
    
# Ingresar al entorno de admin de atenciones 
# Falta agregar permiso
@login_required(login_url='/login/')
def administrarAtencion (request):
    #Cargamos las atenciones del Mecánico que esté logeado
    nombre = request.user.first_name + " " + request.user.last_name
    mensaje = "atenciones de " + nombre
    try:
        listaAtenciones = Atencion.objects.filter(trabajador = nombre)
        # Entregamos un aviso al Mecánico de las publicaciones no publicadas
        cantidad = Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()
        if cantidad == 1:
            cantidad = nombre + " Tienes " + str(Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()) + " Atención sin publicar"
        else:
            cantidad = nombre + " Tienes " + str(Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()) + " Atenciones sin publicar"
        datos = {"atenciones":listaAtenciones, "mensaje":mensaje, "cantidad":cantidad}
    except:
        #Si no encuentra atenciones mandará mensaje sin atenciones
        mensaje = "Sin atenciones"
        datos = {"mensaje":mensaje}
    return render(request,'core/adminAtencion.html',datos)

def pagModificarAtencion(request, id):
    listaCategorias = TipoAtencion.objects.all()
    atencion = Atencion.objects.get(id = id)
    datos = {"categorias":listaCategorias,"atencion":atencion}
    return render(request,'core/modificar-atencion.html',datos)

def actualizar(request):
    nombre_trabajor = request.user.first_name + " " + request.user.last_name
    listaAtenciones = Atencion.objects.filter(trabajador = nombre_trabajor)
    if request.POST:
        id_ate = request.POST.get("txtID")
        diag = request.POST.get("txtDiagnostico")
        fech = request.POST.get("txtFecha")
        img = request.FILES.get("txtImagen")
        mate = request.POST.get("txtMateriales")
        tipo = request.POST.get("cboCategoria")
        obj_tipo = TipoAtencion.objects.get(categoria = tipo)

        nombre = request.user.first_name + " " + request.user.last_name
        cantidad = Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()
        if cantidad == 1:
            cantidad = nombre + " Tienes " + str(Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()) + " Atención sin publicar"
        else:
            cantidad = nombre + " Tienes " + str(Atencion.objects.filter(trabajador = nombre).filter(publicado = False).count()) + " Atenciones sin publicar"
        try:
            a = Atencion.objects.get(id = id_ate )
            a.diagnostico = diag
            a.fecha = fech
            
            # Si no se carga una foto que no la modifique
            if img is not None:
                a.imagen = img

            a.materiales = mate
            a.id_atencion = obj_tipo
            a.save()
            datos = {"atenciones":listaAtenciones, "mensajeUpdate":"Modificado", "cantidad":cantidad}
        except:
            datos = {"atenciones":listaAtenciones, "mensajeUpdate":"No modificado","cantidad":cantidad}
            
    return render (request,'core/adminAtencion.html', datos)

def eliminarAtencion(request,id):
    atencion = Atencion.objects.get(id = id)
    atencion.delete()
    return redirect(to='ADMIN_ATENCION')

'''
   diagnostico = models.TextField(max_length = 40)
    fecha = models.DateField(null=True)
    imagen = models.ImageField(upload_to = 'atenciones', null = True) #Nulo por ahora
    materiales = models.TextField(max_length = 40)
    id_atencion = models.ForeignKey(TipoAtencion, on_delete = CASCADE)
    publicado = models.BooleanField(default = False)
    comentario = models.CharField(max_length = 40, null = True, default = "N/A")
    trabajador = models.CharField(max_length = 30)

'''