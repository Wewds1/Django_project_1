from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contacts/new/', views.contact_create, name='contact_create'),
    path('function', views.hello_world),
    path('class', views.HelloPerson.as_view()),
]