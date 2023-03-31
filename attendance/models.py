from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=100)
    DEPARTMENT_CHOICES = [
        ('BBA', 'BBA'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
    ]
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    SEM_CHOICES = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eighth'),
    ]

    DEPARTMENT_CHOICES = [
        ('BBA', 'BBA'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
    ]
    
    
    sem = models.IntegerField(choices=SEM_CHOICES)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    
    def __str__(self):
        return self.name

    

class Agg_Attendance(models.Model):
    ATTENDANCE_STATUS = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attended_classes = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS)

    def save(self, *args, **kwargs):
        self.total_classes = self.total_classes + 1
        if self.status == 'P':
            self.attended_classes = self.attended_classes + 1
        super(Attendance, self).save(*args, **kwargs)
  
    def __str__(self):
        return self.student.name 
    

class Datewise_Attendance (models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present_in = models.ManyToManyField(Subject, blank=True)
    def __str__(self):
        return self.student.name