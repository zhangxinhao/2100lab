from django.http import HttpResponse
from .models import User, Order, Picture, Course
from django.contrib import auth
import json
import time

def getOrders(request):
  """

  Output an iterable set, composed of dict. The keys' name of dict are: order_id, course_name, price, status and time.

  """
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  list = Order.objects.filter(user_id=user.id).order_by("-time")
  orders = []
  for item in list:
    order = {}
    order_id = item.order_id
    course = item.course
    course_name = course.course_name
    price = course.price
    status = item.status
    time = item.time
    order["order_id"] = order_id
    order["course_name"] = course_name
    order["price"] = price
    order["status"] = status
    order["time"] = time
    orders.append(order)
  return HttpResponse(json.dumps({"orders": orders}))

