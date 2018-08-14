from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
#本数据库中时间均为时间戳，操作记录中除外

class User(AbstractUser):
    id = models.CharField(max_length=11, primary_key=True)
    icon = models.CharField(max_length=150)
    is_V = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    alive = models.BooleanField(default=True)

class Course(models.Model):
    course_id = models.PositiveIntegerField(primary_key=True)
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
    phone_number = models.ForeignKey('User', on_delete=models.CASCADE)
    first_visit = models.PositiveIntegerField()
    last_visit = models.PositiveIntegerField()
    last_time = models.PositiveIntegerField(default=0)

class Order(models.Model):
    order_id = models.PositiveIntegerField(primary_key=True)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    phone_number = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=0)
    time = models.PositiveIntegerField()

class Operation(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    operation = models.CharField(max_length=50)

class Admin_operation_record(models.Model):
    admin_id = models.PositiveIntegerField()
    operation_code = models.ForeignKey('Operation', on_delete=models.CASCADE)
    object = models.PositiveIntegerField()
    time = models.DateTimeField(default=timezone.now)
