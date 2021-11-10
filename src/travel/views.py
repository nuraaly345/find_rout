from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'base.html')

def home(request):
    name = 'Nuraaly'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'About'
    return render(request, 'about.html', {'name': name})