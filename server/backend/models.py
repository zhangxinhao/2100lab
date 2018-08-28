import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 本数据库中时间均为时间戳，操作记录中除外


class User(AbstractUser):
    id = models.CharField(max_length=11, primary_key=True)
    icon = models.ImageField(upload_to='usericon', blank=True, null=True)
    is_V = models.BooleanField(default=False)
    alias = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    manage_right = models.PositiveIntegerField(default=0)
    talking_allowed = models.BooleanField(default=True)

    def set_active(self, active=False):
        self.is_active = active
        self.save()

    def set_alias(self, new_alias):
        self.alias = new_alias
        self.save()

    def set_icon(self, new_icon):
        self.icon = new_icon
        self.save()

    def cannot_talk(self):
        self.talking_allowed = False
        self.save()


class RightsList(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    right = models.CharField(max_length=20)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    burnt_time = models.PositiveIntegerField(default=0)
    message_on = models.BooleanField(default=True)
    audio_url = models.FileField(upload_to='audio', blank=True, null=True)
    profile_url = models.ImageField(
        upload_to='course_picture', blank=True, null=True)
    create_time = models.PositiveIntegerField(default=int(time.time()))
    perpercentage = models.PositiveIntegerField(default=0)


class AudioTemp(models.Model):
    position = models.FileField(upload_to='audio_temp', blank=True, null=True)


class PictureTemp(models.Model):
    position = models.ImageField(
        upload_to='picture_temp', blank=True, null=True)


class Picture(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    postion = models.ImageField(
        upload_to='course_picture', blank=True, null=True)
    start = models.PositiveIntegerField(default=0)


class VisitRecord(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    last_visit = models.PositiveIntegerField()
    last_time = models.PositiveIntegerField(default=0)
    deal_visit_time = models.PositiveIntegerField(default=0)


class Order(models.Model):
    order_id = models.CharField(max_length=50, primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(default=1)
    time = models.PositiveIntegerField(default=int(time.time()))
    sharer = models.CharField(max_length=11)
    charge_id = models.CharField(max_length=30)


class OrderStatus(models.Model):
    status_code = models.PositiveIntegerField(primary_key=True)
    status = models.CharField(max_length=8)


class Operation(models.Model):
    operation_code = models.PositiveIntegerField(primary_key=True)
    operation = models.CharField(max_length=50)


class AdminOperationRecord(models.Model):
    admin_id = models.CharField(max_length=11)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    object = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)


class Message(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    deleted_at = models.DateTimeField(null=True, default=None)

    def _my_delete(self):
        self.deleted_at = timezone.now()
        self.save()


class Comment(models.Model):
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, default=None)

    def _my_delete(self):
        self.deleted_at = timezone.now()
        self.save()


class Attitude(models.Model):
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    like = models.BooleanField(default=True)


class BlackList(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
