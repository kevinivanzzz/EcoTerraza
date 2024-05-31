from django.shortcuts import render


# Create your views here.
def productos(request):
    return render(request, "producto.html")

def nosotros(request):
    return render(request, "nosotros.html")
