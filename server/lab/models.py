from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Client(AbstractUser):
    phone_number = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=20)
    icon = models.CharField(max_length=150)
    is_V = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    alive = models.BooleanField(default=True)

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    profile = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    burnt_time = models.PositiveIntegerField(default=0)
    message_on = models.BooleanField(default=True)

class Audio(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=150)

class Picture(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    postion = models.CharField(max_length=150)

class Visit_record(models.Model):
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    phone_number = models.ForeignKey('Client', on_delete=models.CASCADE)
    first_visit = models.PositiveIntegerField()
    last_visit = models.DateTimeField(auto_now=True)
    last_time = models.PositiveIntegerField(default=0)
