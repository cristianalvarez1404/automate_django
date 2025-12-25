from awd_main.celery import app
import time
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from dataentry.utils import generate_csv_file,send_email_notification

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

@app.task
def export_data_task(model_name):
  try:
    call_command('exportdata', model_name = model_name)  
  except Exception as e:
    raise e
  
  file_path = generate_csv_file(model_name = model_name)
  
  
  
  #Send email with the attachment
  mail_subject = 'Export Data Successfull'
  message = 'Export data successful. Please find the attachment'
  to_email = settings.DEFAULT_EMAIL
  send_email_notification(mail_subject, message, to_email, attachment= file_path)
  
  return 'Export data task executed successfully.'