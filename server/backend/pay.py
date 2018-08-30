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
    """

    A method for alipay for pc.


    Param is a HTTP request:


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed

    - `pingppObject`: a pingpp object of charge

    """
    try:
        user = request.user
        order_no = _create_order_no_(user.id)
        amount, course, extra = _get_info_(request)
        sharer = extra[0]
        url = extra[1]
        charge = pingpp.Charge.create(
            order_no=order_no,
            amount=int(amount),
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
    except TypeError:
        return JsonResponse({"result": 1})


def alipay_phone(request):
    try:
        user = request.user
        order_no = _create_order_no_(user.id)
        amount, course, extra = _get_info_(request)
        sharer = extra[0]
        url = extra[1]
        charge = pingpp.Charge.create(
            order_no=order_no,
            amount=int(amount),
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
    except TypeError:
        return JsonResponse({"result": 1})

def wx_pc(request):
    try:
        user = request.user
        order_no = _create_order_no_(user.id)
        amount, course, extra = _get_info_(request)
        sharer = extra[0]
        try:
            charge = pingpp.Charge.create(
                order_no=order_no,
                amount=int(amount),
                app=dict(id=APP_ID),
                channel="wx_wap",
                currency="cny",
                client_ip=URL,
                subject="2100实验室课程支付",
                body="欢迎购买\"" + course.course_name + "\"课程"
            )
            wx_qr = charge["credential"]["wx_wap"]["wx_wap"]
            _create_order_(user, course, amount, sharer, charge)
            return JsonResponse({"status": 0, "qr": wx_qr})
        except Exception as e:
            print(e)
            return JsonResponse({"status": 1})
    except TypeError:
        return JsonResponse({"result": 1})

def wx_phone(request):
    try:
        user = request.user
        order_no = _create_order_no_(user.id)
        amount, course, extra = _get_info_(request)
        sharer = extra[0]
        charge = pingpp.Charge.create(
            order_no=order_no,
            amount=int(amount),
            app=dict(id=APP_ID),
            channel='wx_wap',
            currency='cny',
            client_ip=URL,
            subject=SUBJECT,
            body="欢迎购买\"" + course.course_name + "\"课程"
        )
        _create_order_(user, course, amount, sharer, charge)
        return JsonResponse({"status": 0, "pingppObject": charge})
    except TypeError:
        return JsonResponse({"result": 1})

def _create_order_no_(user_id):
    return str(int(time.time())) + user_id


def _get_info_(request):
    try:
        info = json.loads(request.POST.get("info"))
        course_id = info["courseId"]
        course = Course.objects.get(pk=course_id)
        amount = course.price * 100
        url = info["successUrl"]
        sharer = info["sharer"]
        return amount, course, [sharer, url]
    except TypeError:
        return JsonResponse({"result": 1})

def _create_order_(user, course, price, sharer, charge):
    try:
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
    except AttributeError:
        return JsonResponse({"result": 1})

def webhooks_charge(request):
    """

    A hook method to be called by the `Pingpp` server when charge successfully.

    Detailed information: https://www.pingxx.com/api

    """
    try:
        body = json.loads(request.body.decode('utf-8'))
        charge = body["data"]["object"]
        if body['type'] == 'charge.succeeded':
            try:
                order = Order.objects.get(charge_id=charge["id"])
                order.status = 0
                sharer = order.sharer
                distribute(sharer, order.course_id, order.price)
                order.save()
                return HttpResponse(status=200)
            except Order.DoesNotExist:
                return HttpResponse(status=500)
        else:
            return HttpResponse(status=500)
    except json.decoder.JSONDecodeError:
        return HttpResponse(status=500)

def webhooks_refund(request):
    """

    A hook method to be called by the `Pingpp` server when refund successfully.

    Detailed information: https://www.pingxx.com/api

    """
    try:
        body = json.loads(request.body.decode("utf-8"))
        charge_id = body["data"]["object"]["id"]
        if body['type'] == 'refund.succeeded':
            try:
                order = Order.objects.get(charge_id=charge_id)
                order.status = 2
                order.save()
                return HttpResponse(status=200)
            except Exception:
                return HttpResponse(status=500)
        else:
            return HttpResponse(status=500)
    except json.decoder.JSONDecodeError:
        return HttpResponse(status=500)

def bonus_pay(request):
    """

    A method to pay with bonus.

    Param is a HTTP POST request:

    - `courseId`


    Return is a HTTP JSON request:

    - `status`: 0 means succeeded, 1 means failed

    """
    course_id = request.POST.get("courseId")
    user = request.user
    status = 0
    try:
        course = Course.objects.get(pk=course_id)
        user.balance = user.balance - course.price
        Order.objects.create(
            order_id=_create_order_no_(user.id),
            course=course,
            user=user,
            price=0,
            status=0,
            sharer="0",
            charge_id="bonus paid"
        )
        user.save()
    except Course.DoesNotExist:
        status = 1
    return JsonResponse({"status": status})
