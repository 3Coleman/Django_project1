from django.shortcuts import render
from django.http import HttpResponse

def start_hello(request):
    return HttpResponse("Hello Django")

# Create your views here.
