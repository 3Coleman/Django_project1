from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start(request):
    variable1={'title':'ARM','year':2024,'summary':'action movie','success': False}
    return render(request,'hello.html',variable1)