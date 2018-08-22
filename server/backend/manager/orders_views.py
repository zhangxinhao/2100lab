from ..models import Order, Order_status
from django.http import HttpResponse
import json

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
