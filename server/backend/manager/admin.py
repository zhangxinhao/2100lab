from django.contrib import auth
from ..models import User, rights_list
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

def __to_Binary__(code):
  str = bin(code)
  str = str[2:]
  size = len(str)
  delta = '0' * (5 - size)
  return delta + str

def authorization_check(request):
  user = request.user
  list = __to_Binary__(user.manage_right)
  rights = {}
  for i in range(len(list)):
    right = rights_list.objects.get(id=i).right
    if list[i] is '1':
      rights[right] = True
    else:
      rights[right] = False
  return HttpResponse(json.dumps({"rights": rights}))
