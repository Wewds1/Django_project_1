from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    
class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)


class Contact(models.Model):
    LEAD = 'lead'
    PROSPECT = 'prospect'
    CUSTOMER = 'customer'

    STATUS_CHOICES = [
        (LEAD, 'Lead'),
        (PROSPECT, 'Prospect'),
        (CUSTOMER, 'Customer'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=LEAD)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'