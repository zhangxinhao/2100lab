from django.contrib import admin
from .models import User, Course, Picture, Visit_record, Order, Operation, Admin_operation_record
from .models import Message, Comment, Attitude, Black_list

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Picture)
admin.site.register(Visit_record)
admin.site.register(Order)
admin.site.register(Operation)
admin.site.register(Admin_operation_record)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Attitude)
admin.site.register(Black_list)
