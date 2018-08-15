from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import json

# Create your views here.
def index(request):
    response = HttpResponse("sean")
    return response

def recommendCourse(request):
  list = Course.objects.filter().order_by('-create_time')
  courses = []
  for i in range(5):
    courses.append(list[i])
  return HttpResponse(json.dumps({"courses": courses}))
