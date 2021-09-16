from django.shortcuts import render
from .forms import ReservationForms

# Create your views here.
def reserve(request):
    reserve_form = ReservationForms()
    if request.method=="POST":
        reserve_form = ReservationForms(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            
    else:
        reserve_form = ReservationForms()
    context={"form":reserve_form}
    return render(request,"reservation/reservation.html",context)
