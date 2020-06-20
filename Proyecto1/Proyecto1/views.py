#primero importar el modulo 
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

#Creando una vista en django
def saludo(request):
    #nombre = "Mario"
    #apellido = "Miranda"
    P1 = Persona("Mario", "Miranda", 21)
    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    fechaActual = datetime.datetime.now()

    documentoExterno = open("Proyecto1/templates/miplantilla.html")
    plantilla = Template(documentoExterno.read())
    documentoExterno.close()

    contexto = Context({"nombrePersona" : P1.nombre, "apellidoPersona" : P1.apellido, "edadPersona" : P1.edad,"fecha" : fechaActual, "temas" : temasDelCurso})

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego")

def fecha(request):
    fechaActual = datetime.datetime.now()

    documento = '''<html>
                        <body>
                            <h1>Fecha y hora actual %s</h1>
                        </body>
                    </html>''' %fechaActual

    return HttpResponse(documento)

def calculaEdad(request, edad, anio): #Para pasar parametros por url
    periodo = anio - 2020
    edadFutura = edad + periodo

    documento = """
                    <html>
                        <body>
                            <h2>En el anio %s tendras %s anios</h2>
                        </body>
                    </html>
                """ %(anio, edadFutura)

    return HttpResponse(documento)