from django.test import TestCase
from backend.models import User, Course, Picture, VisitRecord, Order

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username=13230037688,
            password="Captain Sciencez",
            id=13230037688,
            alias="Captain Sciencez",
            icon="captain/sciencez"
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


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(
            course_id=1,
            course_name='javza',
            description='javzajvajvajvjavjajv',
            content='adadasdzasdasdasdasdasd',
            audio_url='aasdzsa/asdas',
            profile_url='aszdas/aaaa',
        )

    def test_price(self):
        course = Course.objects.get(pk=1)
        price = course.price
        self.assertEqual(price, 0)

    def test_burnt_time(self):
        course = Course.objects.get(pk=1)
        burnt_time = course.burnt_time
        self.assertEqual(burnt_time, 0)

    def test_message_on(self):
        course = Course.objects.get(pk=1)
        message_on = course.message_on
        self.assertEqual(message_on, True)


class PictureTestCase(TestCase):
    def setUp(self):
        my_course = Course.objects.create(
            course_id=1,
            course_name='jaxva',
            description='javxajvajvajvjavjajv',
            content='adadasdxasdasdasdasdasd',
            audio_url='aasdsxa/asdas',
            profile_url='asdxas/aaaa',
        )
        Picture.objects.create(
            course=my_course,
            postion='asdxas/asdasd'
        )

    def test_start(self):
        picture = Picture.objects.get(pk=1)
        start = picture.start
        self.assertEqual(start, 0)


class VisitRecordTestCase(TestCase):
    def setUp(self):
        my_user = User.objects.create_user(
            username=13230037688,
            password="Captaxin Science",
            id=13230037688,
            alias="Captxain Science",
            icon="captxain/science"
        )
        my_course = Course.objects.create(
            course_id=1,
            course_name='jacva',
            description='javacjvajvajvjavjajv',
            content='adadasdcasdasdasdasdasd',
            audio_url='aasdca/asdas',
            profile_url='asdcas/aaaa',
        )
        VisitRecord.objects.create(
            course=my_course,
            user=my_user,
            first_visit=12345,
            last_visit=123444
        )

    def test_last_time(self):
        visit_record = VisitRecord.objects.get(pk=1)
        last_time = visit_record.last_time
        self.assertEqual(last_time, 0)


class OrderTestCase(TestCase):
    def setUp(self):
        my_user = User.objects.create_user(
            username=13230037688,
            password="Captavin Science",
            id=13230037688,
            alias="Captavin Science",
            icon="captaivn/science"
        )
        my_course = Course.objects.create(
            course_id=1,
            course_name='javba',
            description='javbajvajvajvjavjajv',
            content='adadasdbasdasdasdasdasd',
            audio_url='aasdsba/asdas',
            profile_url='asdbas/aaaa',
        )
        Order.objects.create(
            order_id=1,
            course=my_course,
            user=my_user,
            price=10,
            time=123
        )

    def test_status(self):
        order = Order.objects.get(pk=1)
        status = order.status
        self.assertEqual(status, 1)
