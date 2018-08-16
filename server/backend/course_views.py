from .models import User, Course, Picture, Audio
from .message_views import messageBoardDic
from django.http import HttpResponse
from django.core import serializers
from django.contrib import auth

import json

def loadCourse(request):
  course_id = request.POST.get("course_id")
  course = Course.objects.get(pk=course_id)
  pictures = Picture.objects.filter(course=course).order_by("start").values()
  pictures = list(pictures)
  audio = course.audio_url
  mb = messageBoardDic(request)
  course = {"pictures": pictures, "audio": audio, "message": mb["message"], "comment": mb["comment"]}
  return HttpResponse(json.dumps(course))
