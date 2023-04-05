from django.db import models
from attendance.models import Student, Subject, Teacher
# Create your models here.


 
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sessional_index = models.IntegerField()
    marks_obtained = models.DecimalField(max_digits=3, decimal_places=1)
    max_marks = models.DecimalField(max_digits=3, decimal_places=1, default=25)

def __str__(self):
    return f"{self.student.name} {self.subject.name} {self.sessional_index} {self.marks_obtained}/{self.max_marks}"


class univ_result(models.Model):
       
   
   univ_roll_no = models.CharField(max_length=100)
   sem1 = models.CharField(max_length=100, default='NA')
   sem2 = models.CharField(max_length=100, default='NA')
   sem3 = models.CharField(max_length=100, default='NA')
   sem4 = models.CharField(max_length=100, default='NA')
   sem5 = models.CharField(max_length=100, default='NA')
   sem6 = models.CharField(max_length=100, default='NA')
   sem7 = models.CharField(max_length=100, default='NA')
   sem8 = models.CharField(max_length=100, default='NA')
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

   def save(self,*args,**kwargs):
         self.student = Student.objects.get(univ_roll_no=self.univ_roll_no)

   def __str__(self):
        return self.student.name
   

