import json
from django.core.files import File
from django.http import JsonResponse
from backend.models import AudioTemp, AdminOperationRecord
from backend.models import Course, Operation, Picture, PictureTemp


HOUR = 3600


def show_courses(request):
    status = 0
    course_id = request.POST.get("searchId")
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
    return JsonResponse({
        "status": 0, "id": audio_temp.id, "url": audio_temp.position.name})


def upload_course_picture(request):
    upload_picture = request.FILES.get("file")
    picture = PictureTemp(position=upload_picture)
    picture.save()
    return JsonResponse({
        "status": 0, "id": picture.id, "url": picture.position.name})


def upload_course(request):
    status = 0
    form = json.loads(request.POST.get("updateForm"))
    img_info = form["imgInfo"]
    profile_url = None
    for img in img_info:
        if img["start"] == 0:
            profile_url = img["id"]
            break
    try:
        profile = PictureTemp.objects.get(pk=profile_url).position
        audio = AudioTemp.objects.get(pk=form["audioInfo"]["id"]).position
    except (PictureTemp.DoesNotExist, AudioTemp.DoesNotExist) as e:
        print(e)
        status = 1
        return JsonResponse({"status": status})
    course = Course(
        course_name=form["courseTitle"],
        description=form["courseDescription"],
        content=form["courseContain"], price=form["price"],
        message_on=form["messageOn"],
        burnt_time=int(form["destroyTime"]) * HOUR,
        audio_url=File(audio, audio.name.split("/")[-1]),
        profile_url=File(profile, profile.name.split("/")[-1]),
        perpercentage=int(float(form["percentage"]) * 10000)
    )
    audio.close()
    profile.close()
    course.save()
    status = _insert_pictrue_(img_info, course)

    log_user_id = request.user.id
    log_object_id = course.course_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=1),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def edit_course(request):
    try:
        status = 0
        result = ""
        form = json.loads(request.POST.get("updateForm"))
        course_id = form["courseId"]
        img_info = form["imgInfo"]
        img_remove_list = form["imgRemoveList"]
        try:
            _update_pictures_(course_id, img_info, img_remove_list)
            _update_audio_(course_id, form["audioInfo"])
            course = Course.objects.get(course_id=course_id)
            course.course_name = form["courseTitle"]
            course.description = form["courseDescription"]
            course.content = form["courseContain"]
            course.price = form["price"]
            course.message_on = form["messageOn"]
            course.burnt_time = int(form["destroyTime"]) * HOUR
            course.perpercentage = int(float(form["percentage"]) * 10000)
            course.save()
        except Exception as my_e:
            status = 1
            result = str(my_e)
        return JsonResponse({"status": status, "result": result})
    except TypeError:
        return JsonResponse({"result": 1})

def _update_pictures_(course_id, img_info, remove_list):
    course = Course.objects.get(course_id=course_id)
    for img in remove_list:
        dir = img["url"].split("/")[-2]
        if dir == "course_picture":
            try:
                Picture.objects.get(pk=dir["id"]).delete()
            except Picture.DoesNotExist:
                pass
    for img in img_info:
        dir = img["url"].split("/")
        if dir[-2] == "picture_temp":
            picture = PictureTemp.objects.get(pk=img["id"]).position
            pic = Picture()
            pic.postion = File(picture, dir[-1])
            pic.course = course
            pic.start = img["start"]
            picture.close()
            pic.save()
            if pic.start == 0:
                course.profile_url = pic.postion


def _update_audio_(course_id, audio_info):
    course = Course.objects.get(course_id=course_id)
    dir = audio_info["url"].split("/")
    if dir[-2] == "audio_temp":
        audio = AudioTemp.objects.get(pk=audio_info["id"]).position
        course.audio_url = File(audio, dir[-1])
        audio.close()
        course.save()


def _insert_pictrue_(image_list, course):
    try:
        for img in image_list:
            try:
                picture_id = int(img["id"])
                picture = PictureTemp.objects.get(pk=picture_id).position
                pic = Picture()
                name = picture.name.split("/")
                pic.postion = File(picture, name[-1])
                pic.course = course
                pic.start = img["start"]
                picture.close()
                pic.save()
            except Picture.DoesNotExist:
                return 1
        return 0
    except TypeError:
        return JsonResponse({"result": 1})

def preload_course(request):
    try:
        status = 0
        course_info = None
        img_list = None
        img_info = None
        try:
            course_id = json.loads(request.POST.get("courseId"))
            course = Course.objects.get(course_id=course_id)
            course_info = _get_course_info_(course)
            img_list, img_info = _get_picture_list_(course)
        except Course.DoesNotExist:
            status = 1
        return JsonResponse({
            "status": status, "courseInfo": course_info,
            "imgList": img_list, "imgInfo": img_info})
    except TypeError:
        return JsonResponse({"result": 1})

def _get_picture_list_(course):
    try:
        picture_list = Picture.objects.filter(course=course).order_by("-start")
        img_list = []
        img_info = []
        for img in picture_list:
            url = img.postion.name
            img_info.append({
                "id": img.pk, "start": img.start, "url": url})
            img_list.append({
                "name": img.pk,
                "url": url})
        return img_list, img_info
    except (AttributeError, TypeError):
        return JsonResponse({"result": 1})

def _get_course_info_(course):
    try:
        course_info = {
            "courseTitle": course.course_name,
            "courseDescription": course.description,
            "courseContain": course.content,
            "messageOn": course.message_on,
            "price": course.price,
            "destroyTime": course.burnt_time / HOUR,
            "percentage": str(course.perpercentage / 10000),
            "audioUrl": course.audio_url.name
        }
        return course_info
    except AttributeError:
        return JsonResponse({"result": 1})
