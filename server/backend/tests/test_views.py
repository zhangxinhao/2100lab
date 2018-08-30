from django.test import TestCase, RequestFactory
from backend.models import Course, Order, User
from backend.views import recommend_course, brief_free_courses, brief_priced_courses, free_courses, priced_courses
from server.views import random


class ViewsTestCase(TestCase):
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

    def test_recommend_course(self):
        request = self.factory.post('/api/listrecommend/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = recommend_course(request)
        self.assertEqual(response.status_code, 200)

    def test_brief_free_courses(self):
        request = self.factory.post('/api/listfreeindex/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = brief_free_courses(request)
        self.assertEqual(response.status_code, 200)

    def test_brief_priced_courses(self):
        request = self.factory.post('/api/listpricedindex/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = brief_priced_courses(request)
        self.assertEqual(response.status_code, 200)

    def test_free_courses(self):
        request = self.factory.post('/api/listfreecourses/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = free_courses(request)
        self.assertEqual(response.status_code, 200)

    def test_priced_courses(self):
        request = self.factory.post('/api/listpricedcourses/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = priced_courses(request)
        self.assertEqual(response.status_code, 200)

    def test_last_last(self):
        request = self.factory.post('/api/random/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = random(request)
        self.assertEqual(response.status_code, 200)
