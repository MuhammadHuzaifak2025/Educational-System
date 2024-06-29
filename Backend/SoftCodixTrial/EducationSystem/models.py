from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustUser(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    PhoneNumber = models.CharField(max_length=10)
    Address = models.TextField()
    class Meta():
        db_table = 'CustUser'

    def __str__(self):
        return self.User.username

class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    User = models.OneToOneField(CustUser, on_delete=models.CASCADE)

    class Meta ():
        db_table = 'Student'

    def __str__(self):
        return self.User.User.username

class Teacher(models.Model):
    TeacherId = models.AutoField(primary_key=True)
    User = models.OneToOneField(CustUser,on_delete=models.CASCADE)

    class Meta ():
        db_table = 'Teacher'

    def __str__(self):
        return self.User.User.username
class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    Teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    class Meta ():
        db_table = 'Course'
        unique_together = ('CourseName', 'Teacher')
    
    def __str__(self):
        return self.CourseName

class Class(models.Model):
    ClassId = models.AutoField(primary_key=True)
    ClassName = models.CharField(max_length=100)
    Course = models.ManyToManyField(Course)
    Student = models.ManyToManyField(Student)

    class Meta ():
        db_table = 'Class'

    def __str__(self):
        return self.ClassName

class Mark(models.Model):
    MarksId = models.AutoField(primary_key=True)
    Student = models.OneToOneField(Student, on_delete=models.CASCADE)
    Course = models.OneToOneField(Course, on_delete=models.CASCADE)
    Class = models.OneToOneField(Class, on_delete=models.CASCADE)
    Marks = models.PositiveIntegerField()

    class Meta ():
        db_table = 'Mark'

    def __str__(self):
        return self.Student.User.User.username