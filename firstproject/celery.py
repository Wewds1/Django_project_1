import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

app = Celery('firstproject')

# Use a string here so the worker doesn't have to serialize
# the configuration object to transmit it to the worker.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
