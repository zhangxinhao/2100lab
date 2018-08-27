import json
import os
import time
import pingpp
from django.http import JsonResponse, HttpResponse
from .models import Course, Order
from .distribute import distribute

pingpp.api_key = "sk_test_y5qHaPH8i9e1yHGqXLeXXPS0"

pingpp.private_key_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "static/rsa_private.pem")

APP_ID = "app_nfzXTOiPq5G4u9ib"

CHANNELS_WEB = ["alipay_qr", "wx_pub_qr", "alipay_pc_direct"]

URL = "123.206.19.149"

SUBJECT = "2100实验室课程支付"


def alipay_pc(request):
    user = request.user
    order_no = _create_order_no_(user.id)
    amount, course, extra = _get_info_(request)
    sharer = extra[0]
    url = extra[1]
    charge = pingpp.Charge.create(
        order_no=order_no,
        amount=amount,
        app=dict(id=APP_ID),
        channel='alipay_pc_direct',
        currency='cny',
        client_ip=URL,
        subject=SUBJECT,
        body="欢迎购买\"" + course.course_name + "\"课程",
        extra=dict(success_url=url)
    )
    _create_order_(user, course, amount, sharer, charge)
    return JsonResponse({"status": 0, "pingppObject": charge})

def alipay_phone(request):
    user = request.user
    order_no = _create_order_no_(user.id)
    amount, course, extra = _get_info_(request)
    sharer = extra[0]
    url = extra[1]
    charge = pingpp.Charge.create(
        order_no=order_no,
        amount=amount,
        app=dict(id=APP_ID),
        channel='alipay_wap',
        currency='cny',
        client_ip=URL,
        subject=SUBJECT,
        body="欢迎购买\"" + course.course_name + "\"课程",
        extra=dict(
            success_url=url,
            cancel_url=url)
    )
    _create_order_(user, course, amount, sharer, charge)
    return JsonResponse({"status": 0, "pingppObject": charge})

def wx_pc(request):
    user = request.user
    order_no = _create_order_no_(user.id)
    amount, course, extra = _get_info_(request)
    sharer = extra[0]
    charge = pingpp.Charge.create(
        order_no=order_no,
        amount=amount,
        app=dict(id=APP_ID),
        channel="wx_wap",
        currency="cny",
        client_ip=URL,
        subject="2100实验室课程支付",
        body="欢迎购买\"" + course.course_name + "\"课程",
        extra=dict(product_id=order_no)
    )
    wx_qr = charge["credential"]["wx_pub_qr"]
    _create_order_(user, course, amount, sharer, charge)
    return JsonResponse({"status": 0, "qr": wx_qr})

def wx_phone(request):
    user = request.user
    order_no = _create_order_no_(user.id)
    amount, course, extra = _get_info_(request)
    sharer = extra[0]
    charge = pingpp.Charge.create(
        order_no=order_no,
        amount=amount,
        app=dict(id=APP_ID),
        channel='wx_wap',
        currency='cny',
        client_ip=URL,
        subject=SUBJECT,
        body="欢迎购买\"" + course.course_name + "\"课程"
    )
    _create_order_(user, course, amount, sharer, charge)
    return JsonResponse({"status": 0, "pingppObject": charge})

def _create_order_no_(user_id):
    return int(time.time()) + user_id

def _get_info_(request):
    info = json.loads(request.POST.get("info"))
    amount = info["amount"] * 100
    course_id = info["courseId"]
    course = Course.objects.get(pk=course_id)
    url = info["successUrl"]
    sharer = info["sharer"]
    return amount, course, [sharer, url]

def _create_order_(user, course, price, sharer, charge):
    if sharer == int(user.id):
        sharer = 0
    Order.objects.create(
        order_id=charge["order_no"],
        course=course,
        user=user,
        price=price,
        sharer=sharer,
        charge_id=charge["id"]
    )

def webhooks_charge(request):
    body = json.loads(request.body)
    charge = body["data"]["object"]
    try:
        order = Order.objects.get(charge_id=charge["id"])
        order.status = 0
        sharer = order.sharer
        distribute(sharer, order.course_id, order.price)
        order.save()
        return HttpResponse(status=200)
    except Order.DoesNotExist:
        return HttpResponse(status=500)
