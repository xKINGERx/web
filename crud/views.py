from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def count(request):
    return render(request,'count.html')


def new(request):
    data = request.GET['fulltextarea']
    a = data.split()
    full = len(a)
    return render(request, 'new.html',{'fulltext': full,'typeddata': data})

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')
