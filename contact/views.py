from django.shortcuts import render
from .models import Contact
from .form import ContactForm

# Create your views here.

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            new_name=form.cleaned_data["name"]
            new_email=form.cleaned_data["email"]
            new_message=form.cleaned_data["message"]
            new_contact=Contact(name=new_name,email=new_email,content=new_message)
            new_contact.save()
        else:
            form=ContactForm(request.POST)





    
    return render(request,"contact/contact.html")
