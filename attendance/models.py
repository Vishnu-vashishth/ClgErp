from django.db import models
from django.contrib.auth.hashers import make_password



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
    roll = models.CharField(max_length=60)
    univ_roll_no = models.CharField(max_length=100, default=None)
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
        self.roll = f'{self.department}-{self.session[2:]}-{self.univ_roll_no[6:]}'
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
    role = models.CharField(max_length=150,default="Teacher")

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.password = make_password(self.password)
        super(Teacher,self).save(*args, **kwargs)
class Roles(models.Model):
    name = models.CharField(max_length=100,default="Teacher", choices=[('Teacher','Teacher'),('HOD','HOD'),('Principal','Principal'),('CC','Class Coordinator')])
    semester= models.IntegerField(default="All",choices=SEM_CHOICES)
    department = models.CharField(max_length=3,default="All", choices=Student.DEPARTMENT_CHOICES)
    teacher = models.ForeignKey('Teacher', default=None, on_delete=models.CASCADE)
    section = models.CharField(max_length=10,default='All', choices=[('All','All'),('A','A'),('B','B'),('C','C')])
    def __str__(self):
        return f"{self.name}, {self.department}-{ self.semester}-{self.section}"
    def save(self,*args, **kwargs):
        self.teacher.role = self.name
        super().save(*args, **kwargs)

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
    percentage = models.FloatField(default=0)
    # date = models.DateField(auto_now_add=True)

    def save(self,*args, **kwargs):
         
         self.total_classes = total_attendance.objects.get(subject=self.subject,section= self.student.section ).total_classes
         self.percentage = (self.attended_classes/self.total_classes)*100
         super().save(*args, **kwargs)

  
    def __str__(self):
        return self.student.name 
    
class total_attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=0)
    session = models.CharField(max_length=4)
    section = models.CharField(max_length=1,default='A', choices=[('A','A'),('B','B'),('C','C')])

    def save(self,*args, **kwargs):
       
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject.name
    

class Datewise_Attendance (models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present_in = models.ManyToManyField(Subject, blank=True)
    def __str__(self):
        return self.student.name