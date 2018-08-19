from Django.http import HttpResponse
import pingpp
import json
import os

pingpp.api_key = "sk_test_y5qHaPH8i9e1yHGqXLeXXPS0"

pingpp.private_key_path = "static/rsa_private.pem"

app_id = "app_nfzXTOiPq5G4u9ib"

channels_qr = ["alipay_qr", "wx_pub_qr"]

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
  if channel in channels_qr:
    course = request.POST.get("course_name")
    try:
      charge = pingpp.Charge.create(
        order_no="123456789",
        amount=100, #订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        app=dict(id=app_id),
        channel=channel,
        currency="cny",
        client_ip="192.168.55.33",
        subject="2100实验室课程支付",
        body=course
      )
      qr = charge["credential"]["channel"]
      return HttpResponse(json.dumps({"status": 0, "result": qr}))
    except Exception as e:
      return HttpResponse(json.dumps({"status": 1, "result": e}))
  else:
    return HttpResponse(json.dumps({"status": 1, "result": "Channle wrong"}))
