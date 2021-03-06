import json
import requests
from django.contrib import auth
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from .models import User, VisitRecord


def get_code(request):
    password = request.POST.get("password")
    phone_number = request.POST.get('phone_number')
    api_key = "264fb31e3ba88e5c55572dd977b2f372"
    single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "【王康王康】您的验证码是{code}。如非本人操作，请忽略本短信"
    parmas = {
        "apikey": api_key,
        "mobile": phone_number,
        "text": text.format(code=password),
    }
    response = requests.post(single_send_url, data=parmas)
    re_dict = json.loads(response.text)
    return JsonResponse({"result": re_dict})


def authenticate(request):
    phone_number = request.POST.get('phone_number')
    verification_code = request.POST.get('verification_code')
    # This code is 0 means verification pass
    if verification_code == '0':
        user = User.objects.filter(id=phone_number)
        if user:
            user = auth.authenticate(
                request, username=phone_number, password="Captain Science")
        else:
            user = User.objects.create_user(
                username=phone_number,
                email=None,
                password="Captain Science",
                id=phone_number,
                alias="Captain Science",
                icon="usericon/icon.jpg")
            user.save()
        auth.login(request, user)
        usr = {}
        usr['id'] = user.pk
        usr['alias'] = user.alias
        usr['icon'] = user.icon
        return JsonResponse({"result": 0})
    else:
        return JsonResponse({"result": 1})
        # verified wrong


def login(request):
    """

    A method to judge whether user is login


    Parameter is a HTTP `request`


    Return is a HTTP response:

    - `status`: `True` means login, `False` means did not login

    """
    if request.user.is_authenticated:
        return JsonResponse({"status": True})
    return JsonResponse({"status": False})


def logout(request):
    """

    A method to make user logout


    Parameters:

    - A HTTP `request`

    """
    auth.logout(request)
    return JsonResponse({"status": 0})


def delete(request):
    """

    A method to delete user


    Parameters:

    - A HTTP `request`


    Return is a Jsonresponse:

    - `result`: 0

    """
    user = request.user
    user.set_active(False)
    user.save()
    return JsonResponse({"result": 0})


def list_recent_visit(request):
    user = request.user
    record_list = VisitRecord.objects.filter(
        user=user).order_by('-last_visit')
    courses = []
    for record in record_list:
        course = record.course

        courses.append(course)
    return JsonResponse({"courses": courses})


def get_visit_history(request):
    user = request.user
    records = VisitRecord.objects.filter(user=user).order_by("-last_visit")
    history = []
    for record in records:
        course = record.course
        infor = {}
        infor["course_id"] = course.course_id
        infor["course_name"] = course.course_name
        infor["audio_url"] = course.audio_url.name
        infor["profile_url"] = course.profile_url.name
        infor["last_visit"] = record.last_visit
        history.append(infor)
    return JsonResponse({"history": history})


def get_user_infor(request):
    user = request.user
    user = [user]
    response = {}
    response['list'] = json.loads(serialize("json", user))
    return JsonResponse(response)


def set_alias(request):
    new_alias = request.POST.get("newAlias")
    user = request.user
    user.set_alias(new_alias)
    user.save()
    return HttpResponse()


def set_icon(request):
    new_icon = request.FILES.get("file")
    user = request.user
    user.set_icon(new_icon)
    user.save()
    return HttpResponse()


def set_user_data(request):
    set_alias(request)
    set_icon(request)
    get_user_infor(request)
