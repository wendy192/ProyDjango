import datetime
from django.template import Template,Context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

def cursoc(request):
    fechaCurso=datetime.datetime.now()
    return render(request,"CursoC.html",{'dameFecha':fechaCurso})
    