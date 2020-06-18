#primero importar el modulo 
from django.http import HttpResponse
import datetime

#Creando una vista en django
def saludo(request):
    documento = '''<html>
                        <body>
                            <h1>Hola mundo en Django</h1>
                        </body>
                    </html>'''

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