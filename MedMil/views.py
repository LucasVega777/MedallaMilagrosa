from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def empresa(request):
    return render(request, "empresa.html")


def conozcanos(request):
    return render(request, "conozcanos.html")


def servicios(request):
    return render(request, "servicios.html")


def contacto(request):
    return render(request, "contacto.html")


def busqueda(request, query):
    txt = "No se encontraron Resultados acerca de: " + query
    dic = {"respuesta", txt}
    return render(request, "busqueda.html", dic)

def fbusqueda(request):
    return render(request, "busqueda.html")

def agradecimiento(request):
    return render(request, "agradecimiento.html")