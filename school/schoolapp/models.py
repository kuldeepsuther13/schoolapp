from django.db import models

# Create your models here.
class Student(models.Model):
    Id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=140)
    contact_details = models.CharField(max_length=250)

class Parent(models.Model):
    Id = models.AutoField(primary_key= True)
    student = models.ForeignKey(Student ,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    contact_details = models.CharField(max_length=250)

class Teacher(models.Model):
    Id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    subject_taught = models.CharField(max_length=140)
    contact_details = models.CharField(max_length=250)

class Course(models.Model):
    Id = models.AutoField(primary_key= True)
    course_name = models.CharField(max_length=150)
    grade_level = models.CharField(max_length=140)

class Class(models.Model):
    Id = models.AutoField(primary_key= True)
    student = models.ForeignKey(Student ,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher ,on_delete=models.CASCADE)
    schedule = models.CharField(max_length=250)
    room_number = models.CharField(max_length=150)

class Attendance(models.Model):
    Id = models.AutoField(primary_key= True)
    student = models.ForeignKey(Student ,on_delete=models.CASCADE)
    Class = models.ForeignKey(Class,on_delete=models.CASCADE)
    date = models.DateField()
    attendance_status = models.CharField(max_length=250)

class Grades(models.Model):
    Id = models.AutoField(primary_key= True)
    student = models.ForeignKey(Student ,on_delete=models.CASCADE)
    Class = models.ForeignKey(Class,on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=250)
    score = models.IntegerField(max_length=150)
    date = models.DateField()

