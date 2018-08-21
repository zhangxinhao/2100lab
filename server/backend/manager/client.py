from django.http import HttpResponse
from ..models import Visit_record, User

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
      "bonus": str(client["balance"])
    })
  if not len(query):
    query.append({
      "usreId": " ",
      "userAlias": " ",
      "bonus": " "
    })
  return HttpResponse(json.dumps({"query": query}))

def delete(request):
  user_id = request.POST.get("user_id")
  user = User.objects.get(id)
  user.is_acitve = False
  user.save()
  return HttpResponse()

def ban(request):
  user_id = request.POST.get("user_id")
  user = User.objects.get(id)
  user.talking_allowed = False
  user.save()
  return HttpResponse()
