from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
#本数据库中时间均为时间戳，操作记录中除外

class User(AbstractUser):
  id = models.CharField(max_length=11, primary_key=True)
  icon = models.CharField(max_length=150)
  is_V = models.BooleanField(default=False)
  balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  course_right = models.BooleanField(default=False)
  user_right = models.BooleanField(default=False)
  super_right = models.BooleanField(default=False)
  admin_right = models.BooleanField(default=False)

  # alive = models.BooleanField(default=True)

  # def authenticate(self, request, id=None, verification=None **kwargs):
  #   UserModel = get_user_model()
  #   if id is None:
  #     id = kwargs.get(UserModel.USERNAME_FIELD)
  #   try:
  #     user = UserModel._default_manager.get_by_natural_key(id)
  #   except UserModel.DoesNotExist:
  #   else:
  #     if self.check_verificatoin(verification) and self.user_can_authenticate(user):
  #       return user

  # def check_verificatoin(self, verification):


class Course(models.Model):
  course_id = models.PositiveIntegerField(primary_key=True)
  profile = models.CharField(max_length=200)
  content = models.TextField()
  price = models.PositiveIntegerField(default=0)
  burnt_time = models.PositiveIntegerField(default=0)
  message_on = models.BooleanField(default=True)
  audio_url = models.CharField(max_length=150)

class Picture(models.Model):
  course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
  postion = models.CharField(max_length=150)

class Visit_record(models.Model):
  course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  first_visit = models.PositiveIntegerField()
  last_visit = models.PositiveIntegerField(default=first_visit)
  last_time = models.PositiveIntegerField(default=0)

class Order(models.Model):
  order_id = models.PositiveIntegerField(primary_key=True)
  course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  status = models.PositiveIntegerField(default=0)
  time = models.PositiveIntegerField()

class Operation(models.Model):
  code = models.PositiveIntegerField(primary_key=True)
  operation = models.CharField(max_length=50)

class Admin_operation_record(models.Model):
  admin_id = models.CharField(max_length=11)
  operation_code = models.ForeignKey('Operation', on_delete=models.CASCADE)
  object = models.CharField(max_length=11)
  time = models.DateTimeField(default=timezone.now)

class Message(models.Model):
  course = models.ForeignKey('Course', on_delete=models.CASCADE)
  user_id = models.CharField(max_length=11)
  content = models.CharField(max_length=140)
  time = models.DateTimeField(timezone.now)
  likes = models.PositiveIntegerField(default=0)
  dislikes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
  message_id = models.ForeignKey('Message', on_delete=models.CASCADE)
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  content = models.CharField(max_length=140)

class Attitude(models.Model):
  message_id = models.ForeignKey('Message',on_delete=models.CASCADE)
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  like = models.BooleanField(default=True)

class Black_list(models.Model):
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
