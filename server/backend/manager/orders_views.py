import os
import time
import pingpp
from django.http import JsonResponse
from backend.models import Order, OrderStatus, VisitRecord


TOTALSECONDS = 86400

pingpp.api_key = "sk_test_y5qHaPH8i9e1yHGqXLeXXPS0"

pingpp.private_key_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "../static/rsa_private.pem")

APP_ID = "app_nfzXTOiPq5G4u9ib"


def list_order(request):
    """

    A method to list orders.


    Param is a HTTP POST request:

    - `orderNo`: can be None and will return all


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed

    - `orders`: a list consists of order in dict.
    """
    order_no = request.POST.get("orderNo")
    order_list = None
    status = 0
    orders = []
    if order_no and order_no.isdigit():
        try:
            order_list = Order.objects.get(order_id=order_no)
            if order_list:
                time_stamp = time.localtime(order_list.time)
                orders.append({
                    "orderNo": order_list.order_id,
                    "userId": order_list.user_id,
                    "courseId": order_list.course_id,
                    "status": OrderStatus.objects.get(
                        status_code=order_list.status).status,
                    "time": time.strftime(
                        '%Y-%m-%d %H:%M:%S', time_stamp)
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
            print(order.time)
            time_stamp = time.localtime(order.time)
            orders.append({
                "orderNo": order.order_id,
                "userId": order.user_id,
                "courseId": order.course_id,
                "status": OrderStatus.objects.get(
                    status_code=order.status).status,
                "time": time.strftime(
                        '%Y-%m-%d %H:%M:%S', time_stamp)
            })
    return JsonResponse({"status": status, "orders": orders})


def _timestamps_(days):
    """

    An inner method to return timestamp of every day's 0 o'clock `days` before
    today.


    Param:

    - `days`


    Return

    - `time_list`

    - `time_str`
    """
    now_time = int(time.time())
    today = now_time - now_time % TOTALSECONDS + time.timezone
    time_list = []
    time_str = []
    for i in reversed(range(days)):
        that_time = today - i * TOTALSECONDS
        time_list.append(that_time)
        time_str.append(time.strftime("%m-%d", time.localtime(that_time)))
    return time_list, time_str


def _get_pv_(time_list):
    pv_list = []
    for i in range(len(time_list) - 1):
        p_v = VisitRecord.objects.filter(last_visit__gte=time_list[i]).filter(
            last_visit__lt=time_list[i + 1]).values()
        pv_list.append(len(p_v))
    p_v = Order.objects.filter(time__gte=time_list[len(time_list) - 1])
    pv_list.append(len(p_v))
    return pv_list


def _get_vol_(time_list):
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
        time_list, time_str = _timestamps_(days)
        pv_list = _get_pv_(time_list)
    else:
        status = 1
    return JsonResponse({
        "status": status, "PV_list": pv_list, "time": time_str})


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
        time_list, time_str = _timestamps_(days)
        vol_list = _get_vol_(time_list)
    else:
        status = 1
    return JsonResponse({"status": status, "VOL_list": vol_list, "time": time_str})


def refund(request):
    """

    A method to refund
    
    """
    status = 0
    order_no = request.POST.get("orderNo")
    result = "正在退款"
    try:
        order = Order.objects.get(order_id=order_no)
        course = order.course
        user = order.user
        record = VisitRecord.objects.filter(course=course, user=user)
        if record:
            raise Exception("已访问过课程，无法退款")
        charge = pingpp.Charge.retrieve(order.charge_id)
        refund = charge.refunds.create(description="2100实验室课程退款")
        if refund["failure_msg"]:
            msg = refund["failure_msg"]
            pos = msg.find('https')
            result = msg[pos:]
            status = 2
    except Exception as my_e:
        status = 1
        result = str(my_e)
    return JsonResponse({"status": status, "result": result})
