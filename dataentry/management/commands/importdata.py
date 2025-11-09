from django.core.management.base import BaseCommand,CommandError
#from dataentry.models import Student
from django.apps import apps
import csv

#Proposed command - python manage.py importdata file_path model_name
#path => C:\Users\-\Desktop\students_data.csv

class Command(BaseCommand):
  help = 'Import data from .csv file'
  
  def add_arguments(self, parser):
    parser.add_argument("file_path", type=str, help="Path to the CSV file")
    parser.add_argument("model_name", type=str, help="Name of the model")
  
  def handle(self, *args, **kwargs):
    file_path = kwargs['file_path']
    model_name = kwargs['model_name'].capitalize()
    
    model = None
    for app_config in apps.get_app_configs():
      try:
        model = apps.get_model(app_config.label, model_name)
        break
      except LookupError:
        continue
    
    if not model:
      raise CommandError(f'Model "{model_name}" not found in any app!')
    
    with open(file_path,'r',encoding='utf-8') as file:
      reader = csv.DictReader(file)
      
      for row in reader:
        student_exists = model.objects.filter(roll_no = row['roll_no']).exists()
        if not student_exists:
          model.objects.create(**row)
          
    self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))