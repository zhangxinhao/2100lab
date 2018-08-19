from Django.http import HttpResponse
import pingpp
import json
import os

pingpp.api_key = "sk_test_y5qHaPH8i9e1yHGqXLeXXPS0"

pingpp.private_key_path = "static/rsa_private.pem"

app_id = "app_nfzXTOiPq5G4u9ib"

def alyi_qr(request):
  course = request.POST.get("course_name")
  try:
    charge = pingpp.Charge.create(
      order_no='123456789',
      amount=100, #订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
      app=dict(id='app_nfzXTOiPq5G4u9ib'),
      channel='alipay_qr',
      currency='cny',
      client_ip='192.168.55.33',
      subject='2100实验室',
      body='课程'
    )
    qr = charge["credential"]["alipay_qr"]
    return HttpResponse(json.dumps({"status": 0, "result": qr}))
  except Exception as e:
    return HttpResponse(json.dumps({"status": 1, "result": e}))
