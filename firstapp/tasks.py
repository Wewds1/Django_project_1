from celery import shared_task
from django.core.mail import send_mail
from .models import Reservation

@shared_task
def send_reservation_confirmation(reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
        subject = f'Reservation Confirmation for {reservation.first_name}'
        message = f'Hello {reservation.first_name}, your reservation for {reservation.guest_count} guests is confirmed!'
        recipient_list = ['customer@example.com'] # In real world, this would be from the Contact model

        send_mail(subject, message, 'crm@restaurant.com', recipient_list)
        return f'Confirmation email sent for reservation {reservation_id}'
    except Reservation.DoesNotExist:
        return f'Reservation {reservation_id} not found'
