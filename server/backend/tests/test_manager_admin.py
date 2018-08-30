from django.test import TestCase, RequestFactory
from backend.models import User, RightsList, AdminOperationRecord, Operation
from backend.manager.admin_views import authenticate, logout, authorization_check, ban_client
from backend.manager.admin_views import create_admin, get_admin, edit_admin, delete_admin, record_list, access_check

class AdminTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
                username=13230037688,
                password="Cap22ztain Scissence",
                id=13230037688,
                alias="Captai2z2n Sciessnce",
                icon="capta22zn/scienssce"
            )
        Operation.objects.create(
            operation_code='9',
            operation='sadas'
        )
        Operation.objects.create(
            operation_code='10',
            operation='sadsas'
        )
        self.factory = RequestFactory()
        self.user = user

    def test_authenticate(self):
        request = self.factory.post('/api/adminlogin/', {
            'username': '13230037699',
            'password': 'asdas'
        })
        request.user = self.user
        response = authenticate(request)
        self.assertEqual(response.status_code, 200)

    def test_access_check(self):
        request = self.factory.post('/api/accesscheck/')
        request.user = self.user
        response = access_check(request)
        self.assertEqual(response.status_code, 200)

    def test_authorization_check(self):
        request = self.factory.post('/api/authorizationcheck/')
        request.user = self.user
        response = authorization_check(request)
        self.assertEqual(response.status_code, 200)

    def test_ban_client(self):
        request = self.factory.post('/api/shutup/', {
            'userId': '13230037699'
        })
        request.user = self.user
        response = ban_client(request)
        self.assertEqual(response.status_code, 200)

    def test_create_admin(self):
        request = self.factory.post('/api/createadmin/', {
            'adminName': '13230037688'
        })
        request.user = self.user
        response = create_admin(request)
        self.assertEqual(response.status_code, 200)

    def test_get_admin(self):
        request = self.factory.post('/api/getadmin/')
        request.user = self.user
        response = get_admin(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_admin(self):
        request = self.factory.post('/api/editadmin/', {
            'adminId': '13230037688'
        })
        request.user = self.user
        response = edit_admin(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_admin(self):
        request = self.factory.post('/api/deleteadmin/', {
            'adminId': '13230037688'
        })
        request.user = self.user
        response = delete_admin(request)
        self.assertEqual(response.status_code, 200)

    def test_record_list(self):
        request = self.factory.post('/api/recordlist/', {
            'adminId': '13230037688',
            'objectId': '13230037688'
        })
        request.user = self.user
        response = record_list(request)
        self.assertEqual(response.status_code, 200)

