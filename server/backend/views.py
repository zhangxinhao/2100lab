from django.http import JsonResponse
from .models import Course

# Create your views here.


def index(request):
    return JsonResponse({"result": 0})


def recommend_course(request):
    print("in")
    course_list = Course.objects.filter().order_by('-create_time').values()
    courses = []
    size = 5 if len(course_list) > 5 else len(course_list)
    for i in range(size):
        my_course = course_list[i]
        course = {}
        course['id'] = my_course["course_id"]
        course['profile_url'] = my_course["profile_url"]
        courses.append(course)
    return JsonResponse({"courses": courses})


def free_courses(request):
    return list_courses(request, True)


def priced_courses(request):
    return list_courses(request, False)


def brief_free_courses(request):
    return list_courses(request, True, 6)


def brief_priced_courses(request):
    return list_courses(request, False, 6)


def list_courses(request, free=None, number=None):
    course_list = []
    if free is None:
        course_list = Course.objects.filter().order_by("-create_time").values()
    elif free is True:
        course_list = Course.objects.filter(price=0).order_by("-create_time").values()
    else:
        course_list = Course.objects.filter(
            price__gt=0).order_by("-create_time").values()
    courses = []
    end = 0
    _end_ = len(course_list)
    if number is not None:
        if number > _end_:
            end = _end_
        else:
            end = number
    else:
        end = len(course_list)

    for i in range(end):
        course = {}
        my_course = course_list[i]
        course['id'] = my_course.course_id
        course['name'] = my_course.course_name
        course['profile_url'] = my_course.profile_url
        course['description'] = my_course.description
        course['price'] = my_course.price
        courses.append(course)
    courses.append({
        "id": 11,
        "name": "test",
        "profile_url": "/static/img/banner1.8f478db.jpg",
        "description": "Realy test",
        "price": 10
    })
    return JsonResponse({"courses": courses})
