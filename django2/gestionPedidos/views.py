from django.shortcuts import render

from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    if request.GET["producto"]:
        #mensaje="Articulo Buscado: %r" %request.GET["producto"]
        producto = request.GET["producto"]
        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto) # Articulos nombre de la tabla
            return render(request, "resultado_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["jmolina12344@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")
    return render(request, "contacto.html")
    csrf_protect()