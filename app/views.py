from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

def Indian(request):
    return HttpResponse('india is my country')

def python(request):
    return HttpResponse('python is a high level language bcs we can understood esaily and also write the syntax easily')

def king(request):
    return HttpResponse('<h1><marquee>king kohli</marquee></h1>')

def home(request):
    v=loader.get_template('first.html')
    return HttpResponse(v.render())

