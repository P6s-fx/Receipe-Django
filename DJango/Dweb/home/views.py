from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    people = [

        {'name' : 'param','age': 21},
        {'name' : 'Sameer','age': 25},
        {'name' : 'Krishna','age': 22},
        {'name' : 'Ram','age': 26},
        {'name' : 'Sita','age': 41},
    ]
        
    return render(request , "home/index.html",context={'people' : people})

def about(request):
    contaxt = {'page' : 'About'}

    return render(request , "home/about.html")

def contact(request):
    contaxt = {'page' : 'Contact'}
    return render(request , "home/contact.html")