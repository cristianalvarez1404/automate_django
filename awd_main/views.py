from django.shortcuts import render
from django.http import HttpResponse
import time
from dataentry.tasks import celery_test_task 

def home(request):
  return render(request,template_name="home.html")

def celery_test(request):
  # time.sleep(10)  
  celery_test_task.delay()
  return HttpResponse("<h3>Function executed sucessfully</h3>")