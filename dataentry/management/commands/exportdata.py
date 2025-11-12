import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
import datetime

#propsed command = python manage.py exportdata

class Command(BaseCommand):
  help = 'Export data from Student model to a CSV file'
  
  def handle(self, *args, **kwargs):
    # fetch the data from the database
    students = Student.objects.all()
    
    # generate the timestamp of current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # define the csv file name/path
    file_path = f'exported_students_data_{timestamp}.csv'
    
    # open the csv file and write the data
    with open(file_path, 'w', newline='') as file:
      writer = csv.writer(file)
      
      # write the CSV header
      writer.writerow(['Roll No', 'Name', 'Age'])
      
      # write data rows
      for student in students:
        writer.writerow([student.roll_no, student.name, student.age])
        
    self.stdout.write(self.style.SUCCESS("Data exported successfully! ✨🎉"))