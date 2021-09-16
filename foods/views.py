from django.shortcuts import render
from .models import Food,Galery


# Create your views here.
def food_list(request):
    food_list=Food.objects.all()
    galer=Galery.objects.all()
    context={"foods": food_list,"galery":galer}
    return render(request,"foods/list.html",context)

def food_detail(request,id):
    food=Food.objects.get(id=id)
    context={"food":food}
    return render(request,"foods/detail.html",context)

def menu(request):
    food_list=Food.objects.all()
    
    context={"foods": food_list}
    return render(request,"foods/menu.html",context)
def galary(request):
    galer=Galery.objects.all()
    context={"galery":galer}
    return render(request,"foods/galary.html",context)

