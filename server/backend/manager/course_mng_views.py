from django.http import HttpResponse
from ..models import Course, User, Picture
import json

def show_courses(request):
  status = 0
  course_id = request.POST.get("searchId")
  print(course_id)
  list = None
  course_data = []
  if course_id:
    if course_id.isdigit():
      try:
        course = Course.objects.get(course_id=course_id)
        course_data.append({
          "courseId": course.course_id,
          "courseTitle": course.course_name,
          "destroyTime": course.burnt_time,
          "messageRight": course.message_on,
          "coursePrice": course.price
        })
      except Course.DoesNotExist as e:
        status = 0
    else:
      status = 1
  else:
    list = Course.objects.filter().order_by("-create_time")
    for course in list:
      course_data.append({
        "courseId": course.course_id,
        "courseTitle": course.course_name,
        "destroyTime": course.burnt_time,
        "messageRight": course.message_on,
        "coursePrice": course.price
      })
  return HttpResponse(json.dumps({"status": status, "courseData": course_data}))

def upload_audio(request):
  audio = request.FILES.get("file")
  id = request.POST.get("courseid")
  course_title = request.POST.get("course_title")
  course_description = request.POST.get("course_description")
  course_contain = request.POST.get("course_contain")
  course_description = request.POST.get("course_description")
  price = request.POST.get("price")
  destroy_time = request.POST.get("destroy_time")
  coures = Course.objects.create(
      course_id = id,
      course_name = course_title,
      description = course_description,
      content = course_contain,
      price = price,
      burnt_time = destroy_time,
      audio_url = audio,
      )
  coures.save()
  return HttpResponse(json.dumps({"status": 0, "id": id}))

def upload_course(request):
  id = request.POST.get("courseid")
  course_title = request.POST.get("course_title")
  course_description = request.POST.get("course_description")
  course_contain = request.POST.get("course_contain")
  course_description = request.POST.get("course_description")
  price = request.POST.get("price")
  destroy_time = request.POST.get("destroy_time")

  course = Course.objects.get(pk=id)
  course.course_name = course_title
  course.description = course_description
  course.content = course_contain
  course.price = price
  course.burnt_time = destroy_time
  course.save()
  return HttpResponse(json.dumps({"status": 0}))

def upload_course_picture(request):
  upload_picture = request.FILES.get("file")
  id = request.POST.get("courseid")
  course = Course.objects.get(pk=id)
  picture = Picture.objects.create(
    course = course,
    postion = upload_picture
  )
  picture.save()
  return HttpResponse(json.dumps({"status": 0}))
