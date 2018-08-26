import time
from django.http import JsonResponse
from backend.models import Order, OrderStatus, VisitRecord


TOTALSECONDS = 86400


def list_order(request):
    order_no = request.POST.get("orderNo")
    order_list = None
    status = 0
    orders = []
    if order_no and order_no.isdigit():
        try:
            order_list = Order.objects.get(order_id=order_no)
            if order_list:
                orders.append({
                    "orderNo": order_list.order_id,
                    "userId": order_list.user_id,
                    "courseId": order_list.course_id,
                    "status": OrderStatus.objects.get(status_code=order_list.status).status
                })
            else:
                status = 1
        except Order.DoesNotExist:
            status = 1
    elif order_no:
        status = 1
    else:
        order_list = Order.objects.filter().order_by("-time")
        for order in order_list:
            orders.append({
                "orderNo": order.order_id,
                "userId": order.user_id,
                "courseId": order.course_id,
                "status": OrderStatus.objects.get(status_code=order.status).status
            })
    return JsonResponse({"status": status, "orders": orders})


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


def __get_pv__(time_list):
    pv_list = []
    for i in range(len(time_list) - 1):
        p_v = VisitRecord.objects.filter(last_visit__gte=time_list[i]).filter(
            last_visit__lt=time_list[i + 1]).values()
        pv_list.append(len(p_v))
    p_v = Order.objects.filter(time__gte=time_list[len(time_list) - 1])
    pv_list.append(len(p_v))
    return pv_list


def __get_vol__(time_list):
    vol_list = []
    for i in range(len(time_list) - 1):
        vol = Order.objects.filter(time__gte=time_list[i], status=1).filter(
            time__lt=time_list[i + 1]).values()
        vol_list.append(len(vol))
    vol = Order.objects.filter(time__gte=time_list[len(time_list) - 1])
    vol_list.append(len(vol))
    return vol_list


def get_pv(request):
    status = 0
    days = request.POST.get("days")
    if days is None:
        days = 7
    else:
        days = int(days)
    time_list = []
    time_str = []
    pv_list = []
    if isinstance(days, int):
        time_list, time_str = __timestamps__(days)
        pv_list = __get_pv__(time_list)
    else:
        status = 1
    return JsonResponse({"status": status, "PV_list": pv_list, "time": time_str})


def get_vol(request):
    status = 0
    days = request.POST.get("days")
    if days is None:
        days = 7
    else:
        days = int(days)
    time_list = []
    time_str = []
    vol_list = []
    if isinstance(days, int):
        time_list, time_str = __timestamps__(days)
        vol_list = __get_vol__(time_list)
    else:
        status = 1
    return JsonResponse({"status": status, "VOL_list": vol_list, "time": time_str})
