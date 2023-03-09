from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse('<h1>Rohit sharma is known as hitman<h1>')

def surya(request):
    return HttpResponse('<h2> surya is known as sky<h2>')