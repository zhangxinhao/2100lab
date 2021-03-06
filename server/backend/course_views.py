import json
import time
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Course, Order, Picture, VisitRecord
from .message_views import message_board_dic


def load_course(request):
    """

    This function should be called while creating the course page.
    Course's information including URL of pictures and audio,
    content and message board will be returned as dict.

    """
    course_id = request.POST.get("courseId")
    course = Course.objects.get(pk=course_id)
    pictures = Picture.objects.filter(course=course).order_by("start")
    response = {}
    response["pictures"] = json.loads(serialize('json', pictures))
    course = [course]
    response["course"] = json.loads(serialize('json', course))
    message_board = message_board_dic(request)
    if message_board:
        response["message"] = message_board
    return JsonResponse(response)


def get_course_info(request):
    """

    A method to return information of course.


    Param is a HTTP POST request:

    - `courseId`


    Return is a HTTP JSON response:

    - `list`

    - `flags`

    - `userId`

    - `bonus`
    """
    course_id = request.POST.get("courseId")
    try:
        course = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        course = None
    if course:
        course = [course]
    response = {}
    response['list'] = json.loads(serialize('json', course))
    response['flags'] = _get_flags_(course, request.user)
    if request.user.is_authenticated:
        response['userId'] = request.user.id
        response['bonus'] = str(request.user.balance)
    else:
        response['userId'] = 0
        response['bonus'] = 0
    return JsonResponse(response)


def _get_flags_(course, user):
    if user.is_authenticated:
        flags = {
            "isStaff": user.is_staff, "paidFlag": True, "burnedFlag": False}
        if user.is_staff:
            return flags
        print(course[0].price)
        if course[0].price > 0:
            try:
                Order.objects.get(user=user, course=course[0], status=0)
                record = VisitRecord.objects.get(course=course[0], user=user)
                if record.deal_visit_time <= int(time.time()):
                    flags["burnedFlag"] = True
            except Order.DoesNotExist:
                flags["paidFlag"] = False
            except VisitRecord.DoesNotExist:
                flags["burnedFlag"] = False
    else:
        flags = {
            "isStaff": False, "paidFlag": False, "burnedFlag": False
        }
    return flags


def check_course_record(request):
    user = request.user
    course_id = request.POST.get("courseId")
    status = 0
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        status = 1
        return JsonResponse({"status": status})
    try:
        record = VisitRecord.objects.get(user=user, course=course)
        last_time = record.last_time
        deal_visit_time = record.deal_visit_time
        return JsonResponse({
            "lastTime": last_time, "dealVisitTime": deal_visit_time})
    except VisitRecord.DoesNotExist:
        burnt_time = course.burnt_time
        current_time = int(time.time())
        if burnt_time:
            deal_visit_time = burnt_time + current_time
        else:
            deal_visit_time = 2000000000
        VisitRecord.objects.create(
            course=course, user=user, last_visit=current_time, last_time=0,
            deal_visit_time=deal_visit_time)
        return JsonResponse({
            "lastTime": 0, "dealVisitTime": deal_visit_time})


def feedback_course_record(request):
    user = request.user
    course_id = request.POST.get("courseId")
    last_time = request.POST.get("lastTime")
    last_time = float(last_time)
    status = 0
    try:
        course = Course.objects.get(pk=course_id)
        record = VisitRecord.objects.get(user=user, course=course)
        record.last_time = last_time
        record.last_visit = int(time.time())
        record.save()
        return JsonResponse({"status": status})
    except (Course.DoesNotExist, VisitRecord.DoesNotExist):
        status = 1
        return JsonResponse({"status": status})
