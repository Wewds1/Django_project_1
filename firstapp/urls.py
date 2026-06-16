from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contacts/new/', views.contact_create, name='contact_create'),
    path('reservations/new/', views.reservation_create, name='reservation_create'),
    path('reservations/success/', views.reservation_success, name='reservation_success'),
    path('function', views.hello_world),
    path('class', views.HelloPerson.as_view()),
]
