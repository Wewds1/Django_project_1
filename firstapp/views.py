from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.
def hello_world(requests):
    return HttpResponse('Hello World')

class HelloPerson(View):
    def get(self, request):
        return HttpResponse('Hello Person')
    
    