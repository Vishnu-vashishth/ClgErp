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
   sem01 = models.CharField(max_length=100, default='NA')
   sem02 = models.CharField(max_length=100, default='NA')
   sem03 = models.CharField(max_length=100, default='NA')
   sem04 = models.CharField(max_length=100, default='NA')
   sem05 = models.CharField(max_length=100, default='NA')
   sem06 = models.CharField(max_length=100, default='NA')
   sem07 = models.CharField(max_length=100, default='NA')
   sem08 = models.CharField(max_length=100, default='NA')
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

   def save(self,*args,**kwargs):
         self.student = Student.objects.get(univ_roll_no=self.univ_roll_no)
         super().save(*args, **kwargs)

   def __str__(self):
        return self.student.name
   

