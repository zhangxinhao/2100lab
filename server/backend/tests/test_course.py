from django.test import TestCase, RequestFactory
from backend.models import User, Course
from backend.course_views import get_course_info, load_course, feedback_course_record, check_course_record
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
        Course.objects.create(
            course_id=1,
            course_name='java',
            description='javajvajvajvjavjajv',
            content='adadasdasdasdasdasdasd',
            audio_url='aasdsa/asdas',
            profile_url='asdas/aaaa',
        )
        self.user = user
        self.factory = RequestFactory()

    def test_price(self):
        course = Course.objects.get(pk=1)
        price = course.price
        self.assertEqual(price, 0)

    def test_get_course_info(self):
        request = self.factory.post('/api/getcourseinfo/', {
            'courseId': '1'
        })
        request.user = self.user
        response = get_course_info(request)
        self.assertEqual(response.status_code, 200)

    def test_load_course(self):
        request = self.factory.post('/api/coursepage/', {
            'courseId': '1'
        })
        request.user = self.user
        response = load_course(request)
        self.assertEqual(response.status_code, 200)

    def test_feedback_course_record(self):
        request = self.factory.post('/api/feedbackrecord/', {
            'courseId': '1',
            'lastTime': '2'
        })
        request.user = self.user
        response = feedback_course_record(request)
        self.assertEqual(response.status_code, 200)

    def test_check_course_record(self):
        request = self.factory.post('/api/checkrecord/', {
            'courseId': '1',
            'lastTime': '2'
        })
        request.user = self.user
        response = check_course_record(request)
        self.assertEqual(response.status_code, 200)
