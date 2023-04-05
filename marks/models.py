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

