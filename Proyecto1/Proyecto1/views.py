from contextvars import Context
import datetime
from django.template import Template,Context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def cursoc(request):
    fechaCurso=datetime.datetime.now()
    return render(request,"CursoC.html",{'dameFecha':fechaCurso})

def saludo(request): # mi primera vista
    persona1=Persona('Marria','Gomez')
   # nombre='Juan'
  #  apellido='Perez'
    temasDelCurso=['Plantillas','Modelos','Formulario','Vistas','Despliegue']
    ahora=datetime.datetime.now()

    #doc_externo=open('C:/ProyectosDjango/Proyecto1/plantillas/miplantilla.html')
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    doc_externo=loader.get_template('miplantilla.html')
   # ctx=Context({'nombre_persona':persona1.nombre,'apellido_persona':persona1.apellido,'momento_actual':ahora,'temas':temasDelCurso}) # contexto se le pasa al render, puede recibir diccionario
    #doc=plt.render(ctx)
   # doc=doc_externo.render({'nombre_persona':persona1.nombre,'apellido_persona':persona1.apellido,'momento_actual':ahora,'temas':temasDelCurso})

    return render(request,'miplantilla.html',{'nombre_persona':persona1.nombre,'apellido_persona':persona1.apellido,'momento_actual':ahora,'temas':temasDelCurso})

def despedida(request):
    return HttpResponse('Hasta luego a todos ')

def damefecha(request):
    fechaactual=datetime.datetime.now()
    doc="""
    <html>
    <body>
    <H1>
    Fecha y hora actuales %s
    </H1>
    </body>
    </html> """ % fechaactual
    return HttpResponse(doc)

# <html><body></body></html>     <></>   

def calculaEdad(request,edad,agno):
    #edadActual=18
    periodo=agno-2022
    #edadFutura=edadActual+periodo
    edadFutura=edad+periodo
    doc="""<html><body><h2>En el año %s tendras %s años </h2></body></html>""" %(agno,edadFutura)

    return HttpResponse(doc)





