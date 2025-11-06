from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
  help = "It will insert data to the database"
  
  # def add_arguments(self,parser):
  #   parser.add_argument("roll_id",type=str,help="write your roll id")
  #   parser.add_argument("name",type=str,help="write your name")
  #   parser.add_argument("age",type=int,help="write your age")
  
  def handle(self, *args, **kwargs):
    # roll_id = kwargs['roll_id']
    # name = kwargs['name']
    # age = int(kwargs['age'])
    
    dataset = [
      {'role_no':1002,'name':'Name 1','age': 18},
      {'role_no':1003,'name':'Name 2','age': 19},
      {'role_no':1004,'name':'Name 3','age': 20},
      {'role_no':1005,'name':'Name 4','age': 45},
      {'role_no':1006,'name':'Name 5','age': 52},
    ]
    
    try:
      for student in dataset:
        student_exists = Student.objects.filter(roll_no = student['role_no']).exists()
        
        if not student_exists: 
         Student.objects.create(roll_no = student['role_no'],name = student['name'],age =student['age']
          )
         self.stdout.write(self.style.SUCCESS(f"Student with roll id no.{student['role_no']} has been inserted!"))
        else:
          self.stdout.write(self.style.WARNING(f"Student with roll id no.{student['role_no']} already exists!"))
        
      # Student.objects.create(roll_no = roll_id,name = name,age =age)
      self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
    except Exception as e:
      self.stderr.write(self.style.ERROR(f"Error {e}"))
    

