from django.test import TestCase
from backend.models import User, Course, Picture, Visit_record, Order, Message, Attitude

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

class CourseTestCase(TestCase):
  def setUp(self):
    Course.objects.create(
      course_id = 1,
      course_name = 'java',
      description = 'javajvajvajvjavjajv',
      content = 'adadasdasdasdasdasdasd',
      audio_url = 'aasdsa/asdas',
      profile_url = 'asdas/aaaa',
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
      course_id = 1,
      course_name = 'java',
      description = 'javajvajvajvjavjajv',
      content = 'adadasdasdasdasdasdasd',
      audio_url = 'aasdsa/asdas',
      profile_url = 'asdas/aaaa',
    )
    Picture.objects.create(
      course = my_course,
      postion = 'asdas/asdasd'
    )

  def test_start(self):
    picture = Picture.objects.get(pk=1)
    start = picture.start
    self.assertEqual(start, 0)

class Visit_recordTestCase(TestCase):
  def setUp(self):
    my_user = User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
    )
    my_course = Course.objects.create(
      course_id = 1,
      course_name = 'java',
      description = 'javajvajvajvjavjajv',
      content = 'adadasdasdasdasdasdasd',
      audio_url = 'aasdsa/asdas',
      profile_url = 'asdas/aaaa',
    )
    Visit_record.objects.create(
      course = my_course,
      user = my_user,
      first_visit = 12345,
      last_visit = 123444
    )

  def test_last_time(self):
    visit_record = Visit_record.objects.get(pk=1)
    last_time = visit_record.last_time
    self.assertEqual(0, 0)

class OrderTestCase(TestCase):
  def setUp(self):
    my_user = User.objects.create_user(
      username=13230037688,
      password="Captain Science",
      id=13230037688,
      alias="Captain Science",
      icon="captain/science"
    )
    my_course = Course.objects.create(
      course_id = 1,
      course_name = 'java',
      description = 'javajvajvajvjavjajv',
      content = 'adadasdasdasdasdasdasd',
      audio_url = 'aasdsa/asdas',
      profile_url = 'asdas/aaaa',
    )
    Order.objects.create(
      order_id = 1,
      course = my_course,
      user = my_user,
      price = 10,
      time = 123
    )

  def test_status(self):
    order = Order.objects.get(pk=1)
    status = order.status
    self.assertEqual(status, 0)
