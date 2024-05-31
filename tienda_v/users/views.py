from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Usuario
from django.urls import reverse_lazy
from productos.models import Producto
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

def index(request):
    producto = Producto.objects.all()
    context = {'producto': producto}
    return render(request, "index.html", context)

def login_user(request):
    if request.method == 'GET':
       return render(request, "login.html")
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro usuario
            try:
                user = User.objects.create_user(username=request.POST['Usuario'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('login')
            except IntegrityError:
                return render(request, "login.html",{"error": 'El Usuario ya existe'})
        return render(request, "login.html",{"error": 'Las contraseñas no coinciden'})
    
    


def registrarse(request):
    
    if request.method == 'POST':
        usuarios = Usuario() 
        usuarios.nombre = request.POST['nombre']
        usuarios.usuario = request.POST['usuario']
        usuarios.contraseña = request.POST['contraseña']
        usuarios.edad = request.POST['edad']
        usuarios.save()
        return render(request, "login.html")
    return render(request, "registrarse.html")