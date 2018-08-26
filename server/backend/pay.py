import os
from django.http import JsonResponse
import pingpp


pingpp.api_key = "sk_test_y5qHaPH8i9e1yHGqXLeXXPS0"

# pingpp.private_key_path = "../static/rsa_private.pem"

pingpp.private_key_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "static/rsa_private.pem")

APP_ID = "app_nfzXTOiPq5G4u9ib"

CHANNELS_QR = ["alipay_qr", "wx_pub_qr"]


def pay_qr(request):
    """

    A method to pay for course using QR code.
    Parameters needed:
    Paying channel named channel.
    Name of course named course_name.

    Output:
    status: 0: successfule, 1: failed.
    result: url of QR code while status is 0, exception while 1.

    """
    channel = request.POST.get("channel")
    if channel in CHANNELS_QR:
        course = request.POST.get("course_name")
        amount = request.POST.get("amount")
        amt = int(amount) * 100
        status = 0
        result = ""
        if channel == "wx_pub_qr":
            try:
                charge = pingpp.Charge.create(
                    order_no="123456789",
                    amount=amt,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
                    app=dict(id=APP_ID),
                    channel=channel,
                    currency="cny",
                    client_ip="192.168.55.33",
                    subject="2100实验室课程支付",
                    body=course,
                    extra=dict(product_id='course')
                )
                result = charge["credential"][channel]
            except ValueError:
                status = 1
        else:
            try:
                charge = pingpp.Charge.create(
                    order_no="123456789",
                    amount=amt,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
                    app=dict(id=APP_ID),
                    channel=channel,
                    currency="cny",
                    client_ip="192.168.55.33",
                    subject="2100实验室课程支付",
                    body=course
                )
                result = charge["credential"][channel]
            except ValueError:
                status = 1
        return JsonResponse({"status": status, "result": result})
    else:
        return JsonResponse({"status": 1, "result": "Channle wrong"})
