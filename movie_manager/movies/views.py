from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request,'create.html')
def list(request):
    movie_list={'movies':[{'title':'ARM','year':2024,'summary':'action movie','success': True},
                {'title':'Vazha','year':2024,'summary':'love and comedy','success': True},
                {'title':'Janeman','year':2019,'summary':'comedy drama','success': True},
                {'title':'yavanika','year':1984,'summary':'crime thriller','success': False},
                {'title':'CID moosa','year':1984,'summary':'','success': False}]}
    return render(request,'list.html',movie_list)
    
def edit(request):
    return render(request,'edit.html')
