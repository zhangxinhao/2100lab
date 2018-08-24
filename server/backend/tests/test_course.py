from django.test import TestCase, Client, RequestFactory
from backend.models import User, Course

# Create your tests here.


class CourseTestCase(TestCase):
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
      self.user = user
      self.factory = RequestFactory()

    def test_price(self):
      course = Course.objects.get(pk=1)
      price = course.price
      self.assertEqual(price, 0)


