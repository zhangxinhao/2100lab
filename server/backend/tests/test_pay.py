from django.test import TestCase, RequestFactory
from backend.models import Course, Order, User
from backend.pay import webhooks_charge, webhooks_refund, alipay_pc, alipay_phone, wx_pc, wx_phone, bonus_pay, _get_info_, _create_order_

class PayTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=13230037688,
            password="Cap22tain Science",
            id=13230037688,
            alias="Captai22n Science",
            icon="capta22n/science"
        )
        self.factory = RequestFactory()
        self.user = user

    def test_webhooks_charge(self):
        request = self.factory.post('/api/chargewebhooks/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = webhooks_charge(request)
        self.assertEqual(response.status_code, 200)

    def test_webhooks_refund(self):
        request = self.factory.post('/api/refundwebhooks/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = webhooks_refund(request)
        self.assertEqual(response.status_code, 200)

    def test_alipay_pc(self):
        request = self.factory.post('/api/alipaypc/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = alipay_pc(request)
        self.assertEqual(response.status_code, 200)

    def test_alipay_phone(self):
        request = self.factory.post('/api/alipayphone/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = alipay_phone(request)
        self.assertEqual(response.status_code, 200)

    def test_wx_pc(self):
        request = self.factory.post('/api/wxpc/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = wx_pc(request)
        self.assertEqual(response.status_code, 200)

    def test_wx_phone(self):
        request = self.factory.post('/api/wxphone/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = wx_phone(request)
        self.assertEqual(response.status_code, 200)

    def test_bonus_pay(self):
        request = self.factory.post('/api/bonuspay/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = bonus_pay(request)
        self.assertEqual(response.status_code, 200)

    def test_get_info_(self):
        request = self.factory.post('/api/bonuspay/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = _get_info_(request)
        self.assertEqual(response.status_code, 200)

    def test_create_order_(self):
        request = self.factory.post('/api/bonuspay/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = _create_order_(request, self.user, self.user, self.user, self.user)
        self.assertEqual(response.status_code, 200)
