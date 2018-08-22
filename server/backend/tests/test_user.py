from django.test import TestCase, Client
from backend.models import User

# Create your tests here.


class authenticateTestCase(TestCase):
    def setUp(self):
      self.client = Client()

    def test_yes(self):
      response = self.client.post('/api/authenticate/',{
        'phone_number': '13230037688',
        'verification_code': '0'
      })
      self.assertEqual(response.status_code, 200)

    def test_on(self):
      response = self.client.post('/api/authenticate/',{
        'phone_number': '13230037688',
        'verification_code': '1'
      })
      self.assertEqual(response.status_code, 200)

    def test_phone_number(self):
      response = self.client.post('/api/authenticate/',{
        'phone_number': '',
        'verification_code': '1'
      })
      self.assertEqual(response.status_code, 200)

class logoutTestCase(TestCase):
    def setUp(self):
      User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
      )
      self.client = Client()

    def test_yes(self):
      response = self.client.post('/api/logout/')
      self.assertEqual(response.status_code, 200)

class listrecentvisitTestCase(TestCase):
    def setUp(self):
      User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
      )
      self.client = Client()

    def test_yes(self):
      response = self.client.post('/api/listrecentvisit/',{
        'id': '13230037688'
      })
      self.assertEqual(response.status_code, 200)

class setaliasTestCase(TestCase):
    def setUp(self):
      User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
      )
      self.client = Client()

class seticonTestCase(TestCase):
    def setUp(self):
      User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id='13230037688',
      alias="Captain Science",
      icon="captain/science"
      )
      self.client = Client()

