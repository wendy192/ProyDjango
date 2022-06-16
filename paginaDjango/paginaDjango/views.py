import datetime
from django.shortcuts import render 


def cursoc(request):
    fechaCurso=datetime.datetime.now()
    return render(request,"CursoC.html",{'dameFecha':fechaCurso})