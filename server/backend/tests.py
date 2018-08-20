from django.test import TestCase, Client
from .models import User

# Create your tests here.

class UserTestCase(TestCase):
  def setUp(self):
    User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
    )
  def test_is_v(self):
    user = User.objects.get(pk=13230037688)
    is_v = user.is_V
    self.assertEqual(is_v, False)
  def test_balance(self):
    user = User.objects.get(pk=13230037688)
    balance = user.balance
    self.assertEqual(balance, 0)
  def test_manage_right(self):
    user = User.objects.get(pk=13230037688)
    manage_right = user.manage_right
    self.assertEqual(manage_right, 0)

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
    def test_yes(self):
      response = self.client.post('/api/setalias/',{
        'newAlias': 'hehe',
        'id': '13230037688'
      })
      self.assertEqual(response.status_code, 200)

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
    def test_yes(self):
      response = self.client.post('/api/seticon/',{
        'newIcon': 'hehe',
        'id': '13230037688'
      })
      self.assertEqual(response.status_code, 200)
