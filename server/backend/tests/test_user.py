from django.test import TestCase, Client
from backend.models import User

# Create your tests here.


class AuthenticateTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_yes(self):
        response = self.client.post('/api/authenticate/', {
            'phone_number': '13230037688',
            'verification_code': '0'
        })
        self.assertEqual(response.status_code, 200)

    def test_on(self):
        response = self.client.post('/api/authenticate/', {
            'phone_number': '13230037688',
            'verification_code': '1'
        })
        self.assertEqual(response.status_code, 200)

    def test_phone_number(self):
        response = self.client.post('/api/authenticate/', {
            'phone_number': '',
            'verification_code': '1'
        })
        self.assertEqual(response.status_code, 200)


class LogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username=13230037688,
            password="Captain Science1",
            id=13230037688,
            alias="Captain Science1",
            icon="captain/science1"
        )

    def test_yes(self):
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, 200)


class ListrecentvisitTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username=13230037688,
            password="Captain Science2",
            id=13230037688,
            alias="Captain Science2",
            icon="captain/science2"
        )
        self.client = Client()

    def test_yes(self):
        response = self.client.post('/api/listrecentvisit/', {
            'id': '13230037688'
        })
        self.assertEqual(response.status_code, 200)


class SetaliasTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username=13230037688,
            password="Captain Science3",
            id=13230037688,
            alias="Captain Science3",
            icon="captain/science3"
        )
        self.client = Client()


class SeticonTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username=13230037688,
            password="Captain Science4",
            id='13230037688',
            alias="Captain Science4",
            icon="captain/science4"
        )
        self.client = Client()
