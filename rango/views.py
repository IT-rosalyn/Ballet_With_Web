from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    s="Rango say hey there partner! <a href='/rango/about/'>About</a>"
    return HttpResponse(s)

def about(request):
    s1="Rango sayas here is another method <a href='/rango/'>Index</a>"
    return HttpResponse(s1)
