from django.http import HttpResponse
import datetime
from django.template import Template, Context

# ------ Creando URL y URL con Parametros

def saludo(request): #Primera vista
    documento = "<html><body><h1>Hola a todos con django</h1></body></html>"
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """
        <html>
            <body>
                <h2>Hola a todos con django %s </h2>
            </body>
        </html>
    """ % fecha_actual

    return HttpResponse(documento)


# ----- URL con Parametros
def calculaEdad(request, edad, agno):
    #edadActual = 24
    periodo = agno - 2021
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años </h2></body></html>" %(agno, edadFutura)

    return HttpResponse(documento)


# ------- Trabajando con Plantillas
def saludo_2(request):
    doc_externo = open("C:/Users/USER/Desktop/Python_II/django1/django1/plantilla/plantilla.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


# -------- Variables y propiedades en plantillas
def saludo_3(request):
    nombre = "Brehn"
    #apellido = "Contreras"
    fecha = datetime.datetime.now()
    doc_externo = open("C:/Users/USER/Desktop/Python_II/django1/django1/plantilla/plantilla2.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre_persona" : nombre, "apellido_persona" : "Contreras", "fecha" : fecha})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo_4(request):
    p1 = Persona("Jon", "Brehn")

    fecha = datetime.datetime.now()
    doc_externo = open("C:/Users/USER/Desktop/Python_II/django1/django1/plantilla/plantilla3.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "fecha" : fecha})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)