from django.http import HttpResponse
from .models import User
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
      user = User.objects.create_user(username=phone_number, email=None, password=None, id=phone_number)
      user.save()
    auth.login(request, user)
    return HttpResponse(json.dumps({"result": "success", "user": user}))
  else:
    return HttpResponse(json.dumps({"result": "verified wrong"}))

def login(request):
  if request.user.is_authenticated:
    return HttpResponse(json.dumps({"status": True,"user": request.user}))
  else:
    return HttpResponse(json.dumps({"status": False}))

def logout(request):
  auth.logout(request)
  return HttpResponse(json.dumps({"status": False}))
