from django.http import HttpResponse
from ..models import Visit_record, User
from .admin_views import record

import json

def client_history(request):
  """

  A method to show clients' visiting history.

  Parameter is course_id that you want to search, which can be omitted.

  Output is an iterable list named history consisted of dict with three keys:
  course_id, user_id and last_visit.

  PS: The output last_visit is of Unix timestamp.

  """
  course_id = request.POST.get("course_id")
  record = Visit_record.objects.filter()
  if course_id:
    record = record.filter(course_id=course_id)
  record = record.order_by("-last_time").values()
  history = []
  for rcd in record:
    user = User.objects.get(pk=rcd.user_id)
    history.append({
      "course_id": rcd.course_id,
      "user_id": user.id,
      "alias": user.alias,
      "last_visit": rcd.last_visit
    })
  return HttpResponse(json.dumps({"history": history}))

def client_information(request):
  user_id = request.POST.get("user_id")
  print(type(user_id))
  print(user_id)
  user_alias = request.POST.get("user_alias")
  list = None
  searched = False
  if user_id:
    list = User.objects.filter(id=user_id)
    if user_alias:
      list = list.filter(alias=user_alias)
  else:
    if user_alias:
      list = User.objects.filter(alias=user_alias)
  if list is None:
    list = User.objects.filter()
  list = list.values()
  query = []
  for client in list:
    query.append({
      "userId": client["id"],
      "userAlias": client["alias"],
      "bonus": str(client["balance"]),
      "is_V": client["is_V"]
    })
  if not len(query):
    query.append({
      "usreId": " ",
      "userAlias": " ",
      "bonus": " ",
    })
  return HttpResponse(json.dumps({"query": query}))

def delete(request):
  status = 0
  user_id = request.POST.get("user_id")
  try:
    user = User.objects.get(id=user_id)
    user.is_acitve = False
    user.save()
    record(request.user.id, 2, user_id)
  except User.DoesNotExist as e:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def ban(request):
  status = 0
  user_id = request.POST.get("user_id")
  try:
    user = User.objects.get(id=user_id)
    user.talking_allowed = False
    user.save()
    record(request.user.id, 3, user_id)
  except User.DoesNotExist as e:
    status = 1
  return HttpResponse(json.dumps({"status": status}))

def authorize(request):
  status = 0
  user_id = request.POST.get("user_id")
  try:
    user = User.objects.get(id=user_id)
    auth = json.loads(request.POST.get("auth"))
    user.is_V = auth
    user.save()
    record(request.user.id, 4, user_id)
  except User.DoesNotExist as e:
    status = 1
  return HttpResponse(json.dumps({"status": status}))
