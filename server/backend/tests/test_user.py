from django.test import TestCase, Client, RequestFactory
from backend.models import User
from backend.user_views import get_code, login, get_visit_history, get_user_infor, set_alias, set_icon, set_user_data
# Create your tests here.


class AuthenticateTestCase(TestCase):
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
        self.client = Client()

    def test_yes(self):
        response = self.client.post('/api/authenticate/')
        self.assertEqual(response.status_code, 200)

    def test_get_code(self):
        request = self.factory.post('/api/getcode/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = get_code(request)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        request = self.factory.post('/api/login/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = login(request)
        self.assertEqual(response.status_code, 200)

    def test_get_visit_history(self):
        request = self.factory.post('/api/listrecentvisit/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = get_visit_history(request)
        self.assertEqual(response.status_code, 200)

    def test_get_user_infor(self):
        request = self.factory.post('/api/getuserinfo/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = get_user_infor(request)
        self.assertEqual(response.status_code, 200)

    def test_set_alias(self):
        request = self.factory.post('/api/setalias/',{
            'newAlias': 'asdas'
        })
        request.user = self.user
        response = set_alias(request)
        self.assertEqual(response.status_code, 200)

    def test_set_icon(self):
        request = self.factory.post('/api/seticon/')
        request.user = self.user
        response = set_icon(request)
        self.assertEqual(response.status_code, 200)

    def test_set_user_data(self):
        request = self.factory.post('/api/setuserdata/',{
            'newAlias': 'asdas'
        })
        request.user = self.user
        response = set_user_data(request)


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
