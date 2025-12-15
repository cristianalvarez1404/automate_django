from awd_main.celery import app
import time
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings

@app.task
def celery_test_task():
  time.sleep(10)
  #send an email
  mail_subject = 'Test subject'
  message = 'This is a test email'
  from_email = settings.DEFAULT_FROM_EMAIL
  to_email = settings.DEFAULT_TO_EMAIL
  mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
  mail.send()
  return 'Email sent successfully.'

@app.task
def import_data_task(file_path, model_name):
  try:
    call_command('importdata', file_path, model_name)
  except Exception as e:
    raise e
  # notify the user by email
  finally:
    pass
  return 'Data imported successfully.'
