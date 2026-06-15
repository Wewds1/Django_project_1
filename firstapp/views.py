from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from django.views import View

from .forms import ContactForm
from .models import Contact

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
    
