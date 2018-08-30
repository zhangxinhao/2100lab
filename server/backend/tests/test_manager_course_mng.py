from django.test import TestCase, RequestFactory
from backend.models import AudioTemp, AdminOperationRecord, User
from backend.models import Course, Operation, Picture, PictureTemp
from backend.manager.course_mng_views import show_courses, upload_audio, upload_course, upload_course_picture, edit_course, preload_course, _get_course_info_, _get_picture_list_, _insert_pictrue_

class CouseMngTestCaes(TestCase):
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
        self.course = Course.objects.create(
            course_id=2,
            course_name='jadva',
            description='javajdvajvajvjavjajv',
            content='adadasddasdasdasdasdasd',
            audio_url='aasddsa/asdas',
            profile_url='asddas/aaaa',
        )
        self.factory = RequestFactory()
        self.user = user

    def test_show_courses(self):
        request = self.factory.post('/api/showcourse/')
        request.user = self.user
        response = show_courses(request)
        self.assertEqual(response.status_code, 200)

    def test_upload_audio(self):
        request = self.factory.post('/api/uploadaudio/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = upload_audio(request)
        self.assertEqual(response.status_code, 200)

    def test_upload_course_picture(self):
        request = self.factory.post('/api/uploadcoursepicture/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = upload_course_picture(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_course(self):
        request = self.factory.post('/api/editcourse/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = edit_course(request)
        self.assertEqual(response.status_code, 200)

    def test_preload_course(self):
        request = self.factory.post('/api/preload/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = preload_course(request)
        self.assertEqual(response.status_code, 200)

    def test_get_course_info_(self):
        request = self.factory.post('/api/preload/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = _get_course_info_(request)
        self.assertEqual(response.status_code, 200)

    def test_get_picture_list_(self):
        request = self.factory.post('/api/preload/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = _get_picture_list_(request)
        self.assertEqual(response.status_code, 200)

    def test_insert_pictrue_(self):
        request = self.factory.post('/api/preload/', {
            'file': '13230037688'
        })
        request.user = self.user
        response = _insert_pictrue_(request,self.course)
        self.assertEqual(response.status_code, 200)
