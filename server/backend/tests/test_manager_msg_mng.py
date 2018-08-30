from django.test import TestCase, RequestFactory
from backend.models import Message, Comment, AdminOperationRecord, Operation, User
from backend.manager.msg_mng import show_msg, delete_msg

class MsgMngTestCaes(TestCase):
    def setUp(self):
        user = User.objects.create_user(
                username=13230037688,
                password="Cap22ztacdin Scissence",
                id=13230037688,
                alias="Captai2z2n Sciescdsnce",
                icon="capta2cd2zn/scienssce"
            )
        Operation.objects.create(
            operation_code='6',
            operation='sadsas'
        )
        Operation.objects.create(
            operation_code='10',
            operation='sadssas'
        )
        self.factory = RequestFactory()
        self.user = user

    def test_show_msg(self):
        request = self.factory.post('/api/showmessage/')
        request.user = self.user
        response = show_msg(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_msg(self):
        request = self.factory.post('/api/deletemsg/',{
            'msgId': '12'
        })
        request.user = self.user
        response = delete_msg(request)
        self.assertEqual(response.status_code, 200)
