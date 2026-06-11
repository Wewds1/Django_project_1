from django import forms

from .models import Reservation, MenuItem


class reservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'