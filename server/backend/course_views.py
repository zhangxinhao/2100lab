import json
import time
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Course, Picture, VisitRecord
from .message_views import message_board_dic


def load_course(request):
    """

    This function should be called while creating the course page.
    Course's information including URL of pictures and audio,
    content and message board will be returned as dict.

    """
    course_id = request.POST.get("course_id")
    course = Course.objects.get(pk=course_id)
    course_pic = []
    pictures = Picture.objects.filter(course=course).order_by("start")
    for pic in pictures:
        course_pic.append({
            "position": pic.postion,
            "start": pic.start
        })
    course_pic = json.loads(serialize('json', course_pic))
    audio = course.audio_url
    course_description = course.description
    message_board = message_board_dic(request)
    course = {"pictures": course_pic, "audio": audio,
              "message": message_board, "course_description": course_description}
    course = json.loads(serialize('json', course))
    return JsonResponse({"course": course})


def get_course_info(request):
    course_id = request.POST.get("course_id")
    info = {}
    try:
        course = Course.objects.get(course_id=int(course_id))
    except Course.DoesNotExist:
        course = None
    if course:
        info["title"] = course.course_name
        info['description'] = course.description
        info['profile_url'] = course.profile_url
        info['price'] = str(course.price)
    else:
        info["title"] = " "
        info['description'] = " "
        info['profile_url'] = " "
        info['price'] = 0
    info = json.loads(serialize('json', info))
    return JsonResponse(info)


def check_course_record(request):
    user = request.user
    course_id = request.POST("courseId")
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
        deal_visit_time = burnt_time + current_time
        VisitRecord.objects.create(
            course=course, user=user, last_visit=current_time, last_time=0,
            deal_visit_time=deal_visit_time)
        return JsonResponse({
            "lastTime": 0, "dealVisitTime": deal_visit_time})


def feedback_course_record(request):
    user = request.user
    course_id = request.POST("courseId")
    last_time = request.POST("currentTime")
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
