from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import json

# Create your views here.
def index(request):
  response = HttpResponse("sean")
  return response

def recommendCourse(request):
  print("in")
  list = Course.objects.filter().order_by('-create_time').values()
  courses = []
  size = 5 if len(list) > 5 else len(list)
  for i in range(size):
    c = list[i]
    course = {}
    course['id'] = c["course_id"]
    course['profile_url'] = c["profile_url"]
    courses.append(course)
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
    list = Course.objects.filter(price__gt=0).order_by("-create_time").values()
  courses = []
  end = 0
  if number is not None:
    end = number
  else:
    end = len(list)
  if end is 0:
    return HttpResponse(json.dumps({"courses": courses}))
  for i in range(number):
    course = {}
    c = list[i]
    course['id'] = c.course_id
    course['name'] = c.course_name
    course['profile_url'] = c.profile_url
    course['description'] = c.description
    course['price'] = c.price
    courses.append(list[i])
  return HttpResponse(json.dumps({"courses": courses}))
