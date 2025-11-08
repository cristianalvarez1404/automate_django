from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv

#Proposed command - python manage.py importdata file_path
#path => C:\Users\-\Desktop\students_data.csv

class Command(BaseCommand):
  help = 'Import data from .csv file'
  
  def add_arguments(self, parser):
    parser.add_argument("file_path", type=str, help="Path to the CSV file")
  
  def handle(self, *args, **kwargs):
    file_path = kwargs['file_path']
    
    with open(file_path,'r',encoding='utf-8') as file:
      reader = csv.DictReader(file)
      
      for row in reader:
        student_exists = Student.objects.filter(roll_no = row['roll_no']).exists()
        if not student_exists:
          Student.objects.create(**row)
          
    self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))