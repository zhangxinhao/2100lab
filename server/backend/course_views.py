from .models import User, Course, Picture
from .message_views import messageBoardDic
from django.http import HttpResponse
from django.core.serializers import serialize
from django.contrib import auth

import json

def loadCourse(request):
  """

  This function should be called while creating the course page.
  Course's information including URL of pictures and audio, content and message board will be returned as dict.

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
  mb = messageBoardDic(request)
  course = {"pictures": course_pic, "audio": audio, "message": mb, "course_description": course_description}
  course = json.loads(serialize('json', course))
  return HttpResponse(json.dumps({"course": course}))

def getCourseInfo(request):
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
  return HttpResponse(json.dumps(info))
