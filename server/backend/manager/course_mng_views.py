import json
from django.http import JsonResponse
from backend.models import Course, Picture, AudioTemp, PictureTemp


def show_courses(request):
    status = 0
    course_id = request.POST.get("searchId")
    print(course_id)
    course_list = None
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
            except Course.DoesNotExist:
                status = 0
        else:
            status = 1
    else:
        course_list = Course.objects.filter().order_by("-create_time")
        for course in course_list:
            course_data.append({
                "courseId": course.course_id,
                "courseTitle": course.course_name,
                "destroyTime": course.burnt_time,
                "messageRight": course.message_on,
                "coursePrice": course.price
            })
    return JsonResponse({"status": status, "courseData": course_data})


def upload_audio(request):
    audio = request.FILES.get("file")
    audio_temp = AudioTemp(position=audio)
    audio_temp.save()
    return JsonResponse({"status": 0, "id": audio_temp.id})


def upload_course_picture(request):
    upload_picture = request.FILES.get("file")
    picture = PictureTemp(position=upload_picture)
    picture.save()
    return JsonResponse({"status": 0, "id": picture.id})


def upload_course(request):
    status = 0
    form = json.loads(request.POST.get("updateForm"))
    print(type(form))
    audio = None
    profile = None
    profile_url = None
    img_info = form["imgInfo"]
    for img in img_info:
        if img["start"] == 0:
            profile = img["id"]
            break
    print(profile)
    try:
        profile_url = PictureTemp.objects.get(pk=profile)
        print(profile_url)
        audio = AudioTemp.objects.get(pk=form["audioId"])
    except (PictureTemp.DoesNotExist, AudioTemp.DoesNotExist):
        status = 1
        return JsonResponse({"status": status})
    course = Course(
        course_name=form["course_title"],
        description=form["course_description"],
        content=form["course_contain"],
        price=form["price"],
        message_on=form["messageOn"],
        burnt_time=form["destroy_time"],
        audio_url=audio.position,
        profile_url=profile_url.position
    )
    course.save()
    status = _insert_pictrue_(img_info, course)
    return JsonResponse({"status": status})


def _insert_pictrue_(image_list, course):
    for img in image_list:
        try:
            picture_id = int(img["id"])
            picture = PictureTemp.objects.get(pk=picture_id)
            Picture.objects.create(
                course=course, postion=picture.position, start=img["start"])
        except Picture.DoesNotExist:
            return 1
    return 0
