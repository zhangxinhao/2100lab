from django.test import TestCase, Client, RequestFactory
from backend.models import User, Course, Message

# Create your tests here.


class CourseTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=13230037688,
            password="Cap22tain Science",
            id=13230037688,
            alias="Captai22n Science",
            icon="capta22n/science"
        )
        self.client = Client()
        course = Course.objects.create(
            course_id=1,
            course_name='jav22a',
            description='javaj22vajvajvjavjajv',
            content='adadasda22sdasdasdasdasd',
            audio_url='aasd22sa/asdas',
            profile_url='asd22as/aaaa',
        )
        self.user = user
        self.factory = RequestFactory()
        Message.objects.create(
            course=course,
            author=user,
            content='asdasd22asdasdas'
        )

    def test_likes(self):
        message = Message.objects.get(pk=1)
        likes = message.likes
        self.assertEqual(likes, 0)

    def test_dis_likes(self):
        message = Message.objects.get(pk=1)
        dislikes = message.dislikes
        self.assertEqual(dislikes, 0)
