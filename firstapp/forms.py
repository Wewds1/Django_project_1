from django import forms

from .models import Contact, Reservation, MenuItem


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'company', 'status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }