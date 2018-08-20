from .models import User, Course, Picture
from .message_views import messageBoardDic
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth

import json

def loadCourse(request):
  """

  This function should be called while creating the course page.
  Course's information including URL of pictures and audio, content and message board will be returned as dict.

  """
  course_id = request.POST.get("course_id")
  course = Course.objects.get(pk=course_id)
  pictures = Picture.objects.filter(course=course).order_by("start").values()
  pictures = list(pictures)
  audio = course.audio_url
  course_description = course.description
  mb = messageBoardDic(request)
  course = {"pictures": pictures, "audio": audio, "message": mb, "course_description": course_description}
  return HttpResponse(json.dumps({"course": course}))
