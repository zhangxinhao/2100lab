from django.test import TestCase, RequestFactory
from backend.models import Order, OrderStatus, VisitRecord, User
from backend.manager.orders_views import list_order, refund, get_pv, get_vol


class OrdersMngTestCase(TestCase):
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

    def test_list_order(self):
        request = self.factory.post('/api/manageorder/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = list_order(request)
        self.assertEqual(response.status_code, 200)

    def test_get_pv(self):
        request = self.factory.post('/api/getpv/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = get_pv(request)
        self.assertEqual(response.status_code, 200)

    def test_get_vol(self):
        request = self.factory.post('/api/getvol/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = get_vol(request)
        self.assertEqual(response.status_code, 200)

    def test_refund(self):
        request = self.factory.post('/api/refund/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = refund(request)
        self.assertEqual(response.status_code, 200)
