from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start(request):
    movie_list={'movies':[{'title':'ARM','year':2024,'summary':'action movie','success': True},
                {'title':'Vazha','year':2024,'summary':'love and comedy','success': True},
                {'title':'Janeman','year':2019,'summary':'comedy drama','success': True},
                {'title':'yavanika','year':1984,'summary':'crime thriller','success': False},
                {'title':'CID moosa','year':1984,'summary':'','success': False}]}
    return render(request,'hello.html',movie_list)