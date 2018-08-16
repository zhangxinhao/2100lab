from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import json

# Create your views here.
def index(request):
  response = HttpResponse("sean")
  return response

def recommendCourse(request):
  list = Course.objects.filter().order_by('-create_time').values()
  list = list(list)
  courses = []
  for i in range(5):
    courses.append(list[i])
  return HttpResponse(json.dumps({"courses": courses}))

def freeCourses(request):
  return listCourses(request, True)

def pricedCourses(request):
  return listCourses(request, False)

def briefFreeCourses(request):
  return listCourses(request, True, 5)

def briefPricedCourses(request):
  return listCourses(request, False, 5)

def listCourses(request, free=None, number=None):
  list = []
  if free is None:
    list = Course.objects.filter().order_by("-create_time").values()
  elif free is True:
    list = Course.objects.filter(price=0).order_by("-create_time").values()
  else:
    list = Course.objects.filter(price_gt=0).order_by("-create_time").values()
  list = list(list)
  courses = []
  if number is not None:
    for i in range(number):
      courses.append(list[i])
  else:
    courses = list
  return HttpResponse(json.dumps({"courses": courses}))
