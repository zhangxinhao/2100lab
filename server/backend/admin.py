from django.contrib import admin
from .models import User, Course, Picture, VisitRecord, Order, Operation, AdminOperationRecord
from .models import Message, Comment, Attitude, BlackList

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Picture)
admin.site.register(VisitRecord)
admin.site.register(Order)
admin.site.register(Operation)
admin.site.register(AdminOperationRecord)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Attitude)
admin.site.register(BlackList)
