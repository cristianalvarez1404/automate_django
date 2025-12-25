import time
from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task 
from .forms import RegistrationForm

def home(request):
  return render(request,template_name="home.html")

def celery_test(request):
  # time.sleep(10)  
  celery_test_task.delay()
  return HttpResponse("<h3>Function executed sucessfully</h3>")

def register(request):
  if request.method == 'POST':
    return
  else:
    form = RegistrationForm()
    
    context = {
      'form':form  
    }
  return render(request, 'register.html', context=context)