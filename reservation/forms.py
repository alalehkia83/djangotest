from django import forms
from .models import Reservation
class ReservationForms(forms.ModelForm):
    class Meta:
        model=Reservation
        fields="__all__"