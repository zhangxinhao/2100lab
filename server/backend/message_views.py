from django.http import HttpResponse
from .models import User, Course, Message, Comment, Attitude
from django.contrib import auth
import datetime
import json

def messageBoardDic(request):
  """

  An inner method, which shoud not be called directly by the frontend.
  The returned value is dict-typed and serializable. It contains all information of a message board that you may use.

  """
  course = Course.objects.get(request.POST.get("course_id"))
  message = Message.objects.filter(course).order_by("-time").values()
  message = list(message)
  comment = []
  for msg in message:
    comment.extend(list(Comment.objects.filter(message=msg).values()))
  return {"message": message, "comment": comment}

def messageBoard(request):
  """

  Call this method directly to return a serialized value in Json.

  """
  return HttpResponse(json.dumps(messageBoardDic(request)))

def leaveMessage(request):
  """

  A method to leave message. Course id and the message itself are needed.

  """
  time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  course_id = request.POST.get("course_id")
  content = request.POST.get("content")
  course = Course.objects.get(pk=course_id)
  Message.objects.create(course=course, author=user, content=content, time=time)
  return messageBoard(request)

def comment(request):
  """

  A method to make comment. Message id, to which this comment belongs, is needed.

  """
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
  message_id = request.POST.get("message_id")
  content = request.POST.get("content")
  message = Message.objects.get(pk=message_id)
  Comment.objects.create(author=user, message=message, content=content)
  return messageBoard(request)

def express(request):
  """

  Using this method to express you like or dislike. It need a parameter named attitude. "like" means like and same to dislike.

  """
  choice = False
  if request.POST.get("attittude") == "like":
    choice = True
  message_id = request.POST.get('message_id')
  id = request.POST.get("id")
  user = User.objects.get(pk=id)
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
