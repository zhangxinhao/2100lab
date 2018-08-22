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
    try:
      right = rights_list.objects.get(id=i).right
      if list[i] is '1':
        rights[right] = True
      else:
        rights[right] = False
    except rights_list.DoesNotExist as e:
      rights = {
        "course_manage": True,
        "user_manage": True,
        "operation_history": True,
        "order_manage": True,
        "admin_manage": True
      }
  return HttpResponse(json.dumps({"rights": rights}))

def ban_client(request):
  client_id = request.POST.get("userId")
  status = 0
  try:
    user = User.objects.get(id=client_id)
    if user:
      user.cannot_talk()
    else:
      status = 1
  except User.DoesNotExist as e:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def create_admin(request):
  user_name = request.POST.get("adminName")
  status = 0
  try:
    user = User.objects.filter(id=user_name)
    if user:
      stattus = 1
      return HttpResponse(json.dumps({"status": status}))
  except User.DoesNotExist as e:
    status = 0
  rights_code = ['0', '0', '0', '0', '0']
  list = rights_list.objects.filter().values()
  for right in list:
    order = request.POST.get(right['right'])
    if order is str('true'):
      rights_code[right['id']] = '1'
  right = int(''.join(rights_code), 2)
  user = User.objects.create_user(
    username=user_name,
    email=None,
    password=request.POST.get('password'),
    id=user_name,
    is_staff=True,
    is_superuser=True,
    manage_right=right
  )
  user.save()
  return HttpResponse(json.dumps({"status": status}))
