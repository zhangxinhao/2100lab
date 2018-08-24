from django.test import TestCase, Client
from backend.models import Order, User, Course

# Create your tests here.


class OrderTestCase(TestCase):
    def setUp(self):
      user = User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
      )
      self.client = Client()
      course = Course.objects.create(
      course_id = 1,
      course_name = 'java',
      description = 'javajvajvajvjavjajv',
      content = 'adadasdasdasdasdasdasd',
      audio_url = 'aasdsa/asdas',
      profile_url = 'asdas/aaaa',
      )
      Order.objects.create(
        order_id = 1,
        course = course,
        user = user,
        price = 10,
        time = 123
      )

    def test_status(self):
      order = Order.objects.get(pk=1)
      status = order.status
      self.assertEqual(status, 0)

