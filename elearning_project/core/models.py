from django.db import models

# Create your models here.
from django.db import models



class TeacherPage(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
class PostZoomInfo(models.Model):
    text = models.CharField(max_length=50)
    zoom_link = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)

class Emploit(models.Model):
    empl_date = models.DateTimeField()
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)
    post = models.ForeignKey(PostZoomInfo, on_delete=models.CASCADE)

class Video(models.Model):
    name = models.CharField(max_length=50)
    object_key = models.CharField(max_length=255)  # Assuming the object key can be up to 255 characters
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class File(models.Model):
    link = models.CharField(max_length=50)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_postdate = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Follow(models.Model):
    teacher = models.ForeignKey(TeacherPage, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
