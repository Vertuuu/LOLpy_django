from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
