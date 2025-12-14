import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','awd_main.settings')

# Sets up the new celery application for our Django project 'awd_main'
app = Celery('awd_main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result = True)
def debug_task(self):
  print(f"Request: {self.request!r}")