from django.test import TestCase, Client, RequestFactory
from backend.models import Order, User, Course

# Create your tests here.


class OrderTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=13230037688,
            password="Captain Sciencsse",
            id=13230037688,
            alias="Captain Sciessnce",
            icon="captain/sciessnce"
        )
        self.client = Client()
        course = Course.objects.create(
            course_id=1,
            course_name='javssa',
            description='javajvajvssajvjavjajv',
            content='adadasdasssdasdasdasdasd',
            audio_url='aasdsssa/asdas',
            profile_url='asssdas/aaaa',
        )
        Order.objects.create(
            order_id=1,
            course=course,
            user=user,
            price=10,
            time=123,
            sharer=2,
            charge_id='ch_Hm5uTSifDOuTy9iLeLPSurrD'
        )
        self.user = user
        self.factory = RequestFactory()

    def test_status(self):
        order = Order.objects.get(pk=1)
        status = order.status
        self.assertEqual(status, 1)

    def test_get_order(self):
        request = self.factory.post('/api/authenticate/', {
            'phone_number': '13230037688',
            'verification_code': '0'
        })
        request.user = self.user
        response = self.client.post('/api/listorders/')
        self.assertEqual(response.status_code, 200)
