from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def virat(request):
    return HttpResponse('<h1>virat kohli is also known as run machine<h1>')

def abd(request):
    return HttpResponse('<h2>abd is also known as mr 360</h2>')