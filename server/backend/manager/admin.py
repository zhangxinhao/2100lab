from django.contrib import auth
from ..models import User
from django.http import HttpResponse
import json

def authenticate(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = auth.authenticate(request, username = username, password = password)
  status = 0
  if not user:
    status = 1
  elif user.is_staff:
    auth.login(request, user)
  else:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def logout(request):
  auth.logout(request)
  return HttpResponse()
