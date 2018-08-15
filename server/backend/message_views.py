from django.http import HttpResponse, JsonResponse
from .models import User, Course, Message, Comment, Attitude
from django.contrib import auth
import datetime
import json

def messageBoard(request):
  course = Course.objects.get(request.POST.get("course_id"))
  message = Message.objects.filter(course).order_by("-time")
  comment = []
  for msg in message:
    comment.extend(Comment.objects.filter(message=msg))
  return HttpResponse(json.dumps({"message": message, "comment": comment}))

def leaveMessage(request):
  time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  user = request.user
  course_id = request.POST.get("course_id")
  content = request.POST.get("content")
  course = Course.objects.get(pk=course_id)
  Message.objects.create(course=course, author=user, content=content, time=time)
  return messageBoard(request)

def comment(request):
  user = request.user
  message_id = request.POST.get("message_id")
  content = request.POST.get("content")
  message = Message.objects.get(pk=message_id)
  Comment.objects.create(author=user, message=message, content=content)
  return messageBoard(request)

def express(request):
  choice = False
  if request.POST.get("attittude") == "like":
    choice = True
  message_id = request.POST.get('message_id')
  user = request.user
  delta = 0
  message = Message.objects.get(pk=message_id)
  done = Attitude.objects.filter(user=user, message=message, like=choice)
  if not done:
    Attitude.objects.create(user=user, message=message, like=choice)
    delta = 1
  else:
    delta = -2
    done.delete()
  number = 0
  if choice:
    number = message.likes
    number = number + delta
    message.likes = number
  else:
    number = message.dislikes
    number = number + delta
    message.dislikes = number
  message.save()
  return messageBoard(request)
