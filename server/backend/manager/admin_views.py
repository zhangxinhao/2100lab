from django.contrib import auth
from ..models import User, rights_list, Admin_operation_record, Operation
from django.http import HttpResponse
import json
import time

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
  status = 0
  user_name = request.POST.get("adminName")
  try:
    user = User.objects.filter(id=user_name)
    if user:
      status = 1
      return HttpResponse(json.dumps({"status": status}))
  except User.DoesNotExist as e:
    status = 0
  rights_code = ['0', '0', '0', '0', '0']
  list = rights_list.objects.filter().values()
  for right in list:
    order = request.POST.get(right['right'])
    if order == "true":
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

def get_admin(request):
  id = request.POST.get("adminId")
  list = None
  admins = []
  status = 0
  if id:
    try:
      list = User.objects.get(id=id, is_staff=True)
      if list:
        right = __to_Binary__(list.manage_right)
        admin = {
          "adminId": id,
          "password": ''
        }
        try:
          for i in range(len(right)):
            rght = rights_list.objects.get(id=i).right
            if right[i] is '1':
              admin[rght] = True
            else:
              admin[rght] = False
            admins.append(admin[rght])
        except rights_list.DoesNotExist as e:
          status = 1
      else:
        status = 1
    except User.DoesNotExist as e:
      status = 1
  else:
    list = User.objects.filter(is_staff=True).order_by("id").values()
    for admin in list:
      right = __to_Binary__(admin["manage_right"])
      one = {"adminId": admin["id"], "password": ''}
      try:
        for i in range(len(right)):
          rght = rights_list.objects.get(id=i).right
          if right[i] is '1':
            admin[rght] = True
          else:
            admin[rght] = False
          admins.append(admin[rght])
      except rights_list.DoesNotExist as e:
        status = 1
  return HttpResponse(json.dumps({"status": status, "admins": admins}))

def edit_admin(request):
  status = 0
  admin_id = request.POST.get("adminId")
  admin = User.objects.get(id=admin_id)
  if admin:
    rights_code = ['0', '0', '0', '0', '0']
    list = rights_list.objects.filter().values()
    for right in list:
      order = request.POST.get(right['right'])
      if order == 'true':
        rights_code[right['id']] = '1'
    right = int(''.join(rights_code), 2)
    admin.manage_right = right
    password = request.POST.get("password")
    if password:
      admin.set_password(password)
    admin.save()
  else:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def delete_admin(request):
  status = 0
  admin_id = request.POST.get(adminId)
  admin = User.objects.get(id=admin_id)
  if admin:
    admin.setActive()
  else:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def record_list(request):
  status = 0
  admin_id = request.POST.get("adminId")
  object_id = request.POST.get("objectId")
  record = None
  if admin_id:
    record = Admin_operation_record.objects.filter(admin_id=admin_id)
    if object_id:
      record = record.filter(object=object_id)
  elif object_id:
    record = Admin_operation_record.objects.filter(object=object_id)
  else:
    record = Admin_operation_record.objects.filter().order_by("-time")
  history = []
  for data in record:
    try:
      history.append({
        "adminId": data.admin_id,
        "operation": Operation.objects.get(operation_code=data.operation_code).operation,
        "objectId": data.object,
        "time": time.strptime(data.time.timestamp(), "%Y-%m-%d %H:%M:%S")
      })
    except DoesNotExist as e:
      status = 1
  return HttpResponse(json.dumps({"status": status, "history": history}))
