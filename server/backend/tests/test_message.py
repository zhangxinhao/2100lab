from django.test import TestCase, RequestFactory
from backend.models import User, Course, Message, Comment
from backend.message_views import leave_message, comment, express
# Create your tests here.


class MessageTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=13230037688,
            password="Cap22tain Science",
            id=13230037688,
            alias="Captai22n Science",
            icon="capta22n/science"
        )
        course = Course.objects.create(
            course_id=1,
            course_name='jav22a',
            description='javaj22vajvajvjavjajv',
            content='adadasda22sdasdasdasdasd',
            audio_url='aasd22sa/asdas',
            profile_url='asd22as/aaaa',
        )
        message = Message.objects.create(
            course=course,
            author=user,
            content='asdasd22asdasdas'
        )
        Comment.objects.create(
            message=message,
            author=user,
            content='leavecomment'
        )
        self.factory = RequestFactory()
        self.user = user

    def test_likes(self):
        message = Message.objects.get(pk=1)
        likes = message.likes
        self.assertEqual(likes, 0)

    def test_dis_likes(self):
        message = Message.objects.get(pk=1)
        dislikes = message.dislikes
        self.assertEqual(dislikes, 0)

    def test_leave_message(self):
        request = self.factory.post('/api/leaveMessage/', {
            'courseId': '1',
            'content': 'leave message'
        })
        request.user = self.user
        response = leave_message(request)
        self.assertEqual(response.status_code, 200)

    def test_comment(self):
        request = self.factory.post('/api/comment/', {
            'courseId': '1',
            'messageId': '1',
            'content': 'leavecomment'
        })
        request.user = self.user
        response = comment(request)
        self.assertEqual(response.status_code, 200)

    def test_express(self):
        request = self.factory.post('/api/attitude/', {
            'courseId': '1',
            'messageId': '1',
            'attitude': 'dislike'
        })
        request.user = self.user
        response = express(request)
        self.assertEqual(response.status_code, 200)
