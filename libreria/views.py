from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


# Create your views here.
def inicio(request):
 return render(request,'paginas/inicio.html')