from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from django.views import View

from .forms import ContactForm, ReservationForm
from .models import Contact, Reservation
from .tasks import send_reservation_confirmation

# Create your views here.
def hello_world(requests):
    return HttpResponse('Hello World')

class HelloPerson(View):
    def get(self, request):
        return HttpResponse('Hello Person')


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'firstapp/contact_list.html', {'contacts': contacts})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'firstapp/contact_form.html', {'form': form})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # TRIGGER BACKGROUND TASK
            send_reservation_confirmation.delay(reservation.id)
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    return render(request, 'firstapp/reservation_form.html', {'form': form})

def reservation_success(request):
    return HttpResponse('Reservation created successfully! A confirmation email is being sent in the background.')
    
