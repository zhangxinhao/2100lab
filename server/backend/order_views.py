from django.http import HttpResponse
from .models import User, Order, Picture, Course
from django.contrib import auth
import json
import time

def getOrders(request):
  user = request.user
  list = Order.objects.filter(user_id=user.id).order_by("-time")
  orders = []
  for item in list:
    order = {}
    order_id = item.order_id
    course = item.course
    course_name = course.course_name
    price = course.price
    status = item.status
    time_local = time.localtime(item.time)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    order["order_id"] = order_id
    order["course_name"] = course_name
    order["price"] = price
    order["status"] = status
    order["time"] = dt
    orders.append(order)
  return HttpResponse(json.dumps({"orders": orders}))
