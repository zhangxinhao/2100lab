from django.test import TestCase, RequestFactory
from backend.models import VisitRecord, User, AdminOperationRecord, Operation
from backend.manager.client import client_history, client_information, delete, ban, authorize

class ClientTestCaes(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=13230037688,
            password="Cap22tain Scissence",
            id=13230037688,
            alias="Captai22n Sciessnce",
            icon="capta22n/scienssce"
        )
        self.factory = RequestFactory()
        self.user = user

    def test_client_history(self):
        request = self.factory.post('/api/admin_userhistory/', {
            'course_id': '1'
        })
        request.user = self.user
        response = client_history(request)
        self.assertEqual(response.status_code, 200)

    def test_client_information(self):
        request = self.factory.post('/api/clientinfor/', {
            'user_id': '13230037688',
            'user_alias': 'Captai22n Sciessnce'
        })
        request.user = self.user
        response = client_information(request)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        request = self.factory.post('/api/deleteclient/', {
            'user_id': '1323003688'
        })
        request.user = self.user
        response = delete(request)
        self.assertEqual(response.status_code, 200)

    def test_ban(self):
        request = self.factory.post('/api/banclient/', {
            'user_id': '1323003688'
        })
        request.user = self.user
        response = ban(request)
        self.assertEqual(response.status_code, 200)

    def test_authorize(self):
        request = self.factory.post('/api/authorize/', {
            'user_id': '1323003688'
        })
        request.user = self.user
        response = authorize(request)
        self.assertEqual(response.status_code, 200)
