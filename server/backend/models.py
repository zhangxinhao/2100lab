from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import time
# Create your models here.
#本数据库中时间均为时间戳，操作记录中除外

class User(AbstractUser):
  id = models.CharField(max_length=11, primary_key=True)
  icon = models.ImageField(upload_to='usericon', blank=True, null=True)
  is_V = models.BooleanField(default=False)
  alias = models.CharField(max_length=15)
  balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  manage_right = models.PositiveIntegerField(default=0)
  talking_allowed = models.BooleanField(default=True)

  def setActive(self, active=False):
    self.is_active = active
    self.save()

  def setAlias(self, newAlias):
    self.alias = newAlias
    self.save()

  def setIcon(self, newIcon):
    self.icon = newIcon
    self.save()

  def cannot_talk(self):
    self.talking_allowed = False
    self.save()

class rights_list(models.Model):
  id = models.PositiveIntegerField(primary_key=True)
  right = models.CharField(max_length=20)

class Course(models.Model):
  course_id = models.PositiveIntegerField(primary_key=True)
  course_name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  content = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  burnt_time = models.PositiveIntegerField(default=0)
  message_on = models.BooleanField(default=True)
  audio_url = models.CharField(max_length=150)
  profile_url = models.CharField(max_length=150)
  create_time = models.PositiveIntegerField(default=int(time.time()))

class Picture(models.Model):
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
  postion = models.CharField(max_length=150)
  start = models.PositiveIntegerField(default=0)

class Visit_record(models.Model):
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  first_visit = models.PositiveIntegerField()
  last_visit = models.PositiveIntegerField()
  last_time = models.PositiveIntegerField(default=0)

class Order(models.Model):
  order_id = models.PositiveIntegerField(primary_key=True)
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  price = models.PositiveIntegerField()
  status = models.PositiveIntegerField(default=0)
  time = models.PositiveIntegerField()

class Order_status(models.Model):
  status_code = models.PositiveIntegerField(primary_key=True)
  status = models.CharField(max_length=6)

class Operation(models.Model):
  operation_code = models.PositiveIntegerField(primary_key=True)
  operation = models.CharField(max_length=50)

class Admin_operation_record(models.Model):
  admin_id = models.CharField(max_length=11)
  operation_code = models.ForeignKey('Operation', on_delete=models.CASCADE)
  object = models.CharField(max_length=11)
  time = models.DateTimeField(default=timezone.now)

class Message(models.Model):
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
  author = models.ForeignKey('User', on_delete=models.CASCADE)
  content = models.CharField(max_length=140)
  time = models.DateTimeField(default=timezone.now)
  likes = models.PositiveIntegerField(default=0)
  dislikes = models.PositiveIntegerField(default=0)
  deleted_at = models.DateTimeField(null=True, default=None)

  def delete(self):
    self.deleted_at = timezone.now()
    self.save()

class Comment(models.Model):
  message = models.ForeignKey('Message', on_delete=models.CASCADE)
  author = models.ForeignKey('User', on_delete=models.CASCADE)
  content = models.CharField(max_length=140)
  time = models.DateTimeField(default=timezone.now)
  deleted_at = models.DateTimeField(null=True, default=None)

  def delete(self):
    self.deleted_at = timezone.now()
    self.save()

class Attitude(models.Model):
  message = models.ForeignKey('Message',on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  like = models.BooleanField(default=True)

class Black_list(models.Model):
  user = models.ForeignKey('User', on_delete=models.CASCADE)
