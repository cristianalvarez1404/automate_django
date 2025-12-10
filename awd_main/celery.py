import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj.settings')

# Sets up the new celery application for our Django project 'awd_main'
app = Celery('awd_main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()