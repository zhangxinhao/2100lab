from ..models import Order, Order_status, Visit_record
from django.http import HttpResponse
import json
import time

TOTALSECONDS = 86400

def list_order(request):
  order_no = request.POST.get("orderNo")
  list = None
  status = 0
  orders = []
  if order_no and order_no.isdigit():
    try:
      list = Order.objects.get(order_id=order_no)
      if list:
        orders.append({
          "orderNo": list.order_id,
          "userId": list.user_id,
          "courseId": list.course_id,
          "status": Order_status.objects.get(status_code=list.status).status
        })
      else:
        status = 1
    except Order.DoesNotExist as e:
      status = 1
  elif order_no:
    status = 1
  else:
    list = Order.objects.filter().order_by("-time")
    for order in list:
      orders.append({
        "orderNo": order.order_id,
        "userId": order.user_id,
        "courseId": order.course_id,
        "status": Order_status.objects.get(status_code=order.status).status
      })
  return HttpResponse(json.dumps({"status": status, "orders": orders}))

def __timestamps__(days):
  now_time = int(time.time())
  today = now_time - now_time % TOTALSECONDS + time.timezone
  time_list = []
  time_str = []
  for i in reversed(range(days)):
    that_time = today - i * TOTALSECONDS
    time_list.append(that_time)
    time_str.append(time.strftime("%m-%d", time.localtime(that_time)))
  return time_list, time_str

def __get_PV__(time_list):
  PV_list = []
  for i in range(len(time_list) - 1):
    pv = Visit_record.objects.filter(last_visit__gte=time_list[i]).filter(last_visit__lt=time_list[i + 1]).values()
    PV_list.append(len(pv))
  pv = Order.objects.filter(time__gte=time_list[len(time_list) - 1])
  PV_list.append(len(pv))
  return PV_list

def __get_VOL__(time_list):
  VOL_list = []
  for i in range(len(time_list) - 1):
    vol = Order.objects.filter(time__gte=time_list[i], status=1).filter(time__lt=time_list[i + 1]).values()
    VOL_list.append(len(vol))
  vol = Order.objects.filter(time__gte=time_list[len(time_list) - 1])
  VOL_list.append(len(vol))
  return VOL_list

def get_PV(request):
  status = 0
  days = request.POST.get("days")
  if days is None:
    days = 7
  else:
    days = int(days)
  time_list = []
  time_str = []
  PV_list = []
  if isinstance(days, int):
    time_list, time_str = __timestamps__(days)
    PV_list = __get_PV__(time_list)
  else:
    status = 1
  return HttpResponse(json.dumps({"status": status, "PV_list": PV_list, "time": time_str}))

def get_VOL(request):
  status = 0
  days = request.POST.get("days")
  if days is None:
    days = 7
  else:
    days = int(days)
  time_list = []
  time_str = []
  VOL_list = []
  if isinstance(days, int):
    time_list, time_str = __timestamps__(days)
    VOL_list = __get_VOL__(time_list)
  else:
    status = 1
  return HttpResponse(json.dumps({"status": status, "VOL_list": VOL_list, "time": time_str}))
