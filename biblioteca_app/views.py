from django.shortcuts import get_object_or_404, render,redirect
from .models import Categoria,Libro,Prestamo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required

def home(request):
    categoria = Categoria.objects.all()
    usuario = request.user
    return render(request,'categorias.html',{'categoria':categoria,'usuario':usuario})


def loginpage(request):
    if (request.method == 'POST'):
        username= request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
           user = authenticate(request,password=password,username=username)
           if user is not None:
               login(request,user)
               messages.info(request,'Iniciaste sesion')
               return redirect('categorias/')
           
        messages.warning(request,'nombre y/o contraseña incorrectos')
    return render(request,'login.html')

def registro(request):
    if request.method == 'POST':
        usuario_nuevo = request.POST.get('username')
        email_nuevo = request.POST.get('mail')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('chek_password')
        
        if pass1 != pass2:
            messages.warning(request, 'Las contraseñas no coinciden')
            return redirect('registro')  
        
        # Verifica si ya existe un usuario con el mismo nombre de usuario o correo electrónico
        if User.objects.filter(username=usuario_nuevo).exists():
            messages.warning(request, 'El nombre de usuario ya está en uso')
            return redirect('registro')  

        if User.objects.filter(email=email_nuevo).exists():
            messages.warning(request, 'El correo electrónico ya está en uso')
            return redirect('registro')  

        user = User.objects.create_user(username=usuario_nuevo, email=email_nuevo, password=pass1)
        messages.success(request, 'Registro exitoso')
        return redirect('login')  

    return render(request, 'registro.html')


def logoutUser(request):
    if request.method=='GET' and request.user.is_authenticated==True :
        messages.info(request,"Cerraste Sesion")
        return redirect('/')
    
@login_required 
def mostrar_categoria(request,categoria_id): 
    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')
        usuario = request.user
        retiro = timezone.now()
        reintegro = retiro + timedelta(days=7)

        prestamo = Prestamo(libro_id=libro_id,usuario=usuario,retiro=retiro,reintegro=reintegro)
        prestamo.save()
        messages.success(request,'libro alquilado')

    libros = Libro.objects.filter(categoria = categoria_id)
    
    categoria = get_object_or_404(Categoria,pk=categoria_id)

    return render(request,'categoria.html',{'categoria':categoria,'libros':libros})

@login_required
def prestamos(request):
    user = request.user
    prestamos = Prestamo.objects.filter(usuario=user)

    return render (request,'usuario_prestamos.html',{'prestamos':prestamos})


    