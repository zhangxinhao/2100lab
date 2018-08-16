from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import User, Visit_record, Picture, Course
from django.contrib import auth
import json

def authenticate(request):
  phone_number = request.POST.get('phone_number')
  verification_code = request.POST.get('verification_code')
  #This code is 0 means verification pass
  if not verification_code :
    user = User.objects.filter(id=phone_number)
    if user:
      user = auth.authenticate(request, username=phone_number)
    else:
      user = User.objects.create_user(username=phone_number, email=None, password=None, id=phone_number, nickname="科学小队长")
      user.save()
    auth.login(request, user)
    user = model_to_dict(user)
    return HttpResponse(json.dumps({"result": 0, "user": user}))
  else:
    return HttpResponse(json.dumps({"result": 1}))
    #verified wrong

def login(request):
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  if user.is_authenticated:
    user = model_to_dict(user)
    return HttpResponse(json.dumps({"status": True,"user": user}))
  else:
    return HttpResponse(json.dumps({"status": False}))

def logout(request):
  auth.logout(request)
  return HttpResponse(json.dumps({"status": False}))

def delete(request):
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  user.setActive(False)
  user.save()
  return HttpResponse(json.dumps({"result": 0}))

def listRecentVisit(request):
  # id = request.POST.get("id")
  # user = User.objects.get(pk=id)
  # record_list = Visit_record.objects.filter(user=user).order_by('-last_visit')
  # courses = []
  # for record in record_list:
  #   course = Course.objects.get(pk=record.course_id)
  #   course = model_to_dict(course)
  #   courses.append(course)
  # return HttpResponse(json.dumps({"courses": courses}))
  response = HttpResponse("xinhao")
  return response

def getVisitHistory(request):
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  record = Visit_record.objects.filter(user=user).order_by("-last_visit")
  history = []
  for r in record:
    course = r.course
    infor = {}
    infor["course_id"] = course.course_id
    infor["course_name"] = course.course_name
    infor["audio_url"] = course.audio_url
    infor["profile_url"] = course.profile_url
    infor["last_visit"] = r.last_visit
    history.append(infor)
  return HttpResponse(json.dumps({"history": history}))

def getUserInfor(request):
  # id = request.POST.get("id")
  # user = User.objects.get(pk=id)
  # phone_number = user.id
  # nickname = user.nickname
  # icon = user.icon
  # is_V = user.is_V
  # balance = user.balance
  # return HttpResponse(json.dumps({"phone_number": phone_number, "nickname": nickname, "icone": icon, "is_v": is_V, "balance": balance}))
  response = HttpResponse("xinhao")
  return response

def setNickname(request):
  newNickname = request.POST.get("newNickname")
  # id = request.POST.get("id")
  # user = User.objects.get(pk=id)
  # user.setNickname(newNickname)
  # user.save()
  return HttpResponse(json.dumps({"result": 0}))

def setIcon(request):
  newIcon = request.POST.get("newIcon")
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  user.setIcon(newIcon)
  user.save()
  return HttpResponse(json.dumps({"result": 0}))
