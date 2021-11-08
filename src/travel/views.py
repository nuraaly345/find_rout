from django.shortcuts import render

def home(request):
    name = 'Nuraaly'
    return render(request, 'home.html', {'name': 'name'})