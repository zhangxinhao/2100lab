from django.http import HttpResponse
from ..models import Course, User
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
