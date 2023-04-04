from django.db import models
from django.contrib.auth.hashers import make_password





class Student (models.Model):
    name = models.CharField(max_length=100)
    DEPARTMENT_CHOICES = [
        ('BBA', 'BBA'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
    ]
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
    
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    roll = models.IntegerField()
    section = models.CharField(max_length=1,default='A', choices=[('A','A'),('B','B'),('C','C')])
    session = models.CharField(max_length=4, default=None)                           
    curent_sem = models.IntegerField(default =1,choices=SEM_CHOICES)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=100)
    otp = models.CharField(max_length=6,default=None,null=True,blank=True)
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def increaseSem(self):
        self.curent_sem = self.curent_sem + 1
        self.save()
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    otp = models.CharField(max_length=6,default=None,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.password = make_password(self.password)
        super(Teacher,self).save(*args, **kwargs)
 

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
        ('P', 'P'),
        ('A', 'A'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attended_classes = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)
    status = models.CharField(max_length=1,default='A', choices=ATTENDANCE_STATUS)

    def save(self,*args, **kwargs):
         
         self.total_classes = total_attendance.objects.get(subject=self.subject).total_classes
         super().save(*args, **kwargs)

  
    def __str__(self):
        return self.student.name 
    
class total_attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=0)
    session = models.CharField(max_length=4)

    def save(self,*args, **kwargs):
        self.total_classes = self.total_classes + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student.name
    

class Datewise_Attendance (models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present_in = models.ManyToManyField(Subject, blank=True)
    def __str__(self):
        return self.student.name