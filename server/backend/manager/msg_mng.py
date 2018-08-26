from django.http import HttpResponse
from ..models import User, Message, Comment
from .admin_views import record
import datetime
import json

def __querysort__(message, comment):
  return message.extend(comment)

def show_msg(request):
  course_id = request.POST.get("course_id")
  client_id = request.POST.get("client_id")
  message_list = Message.objects.filter(deleted_at=None)
  comment_list = Comment.objects.filter(deleted_at=None)
  if course_id:
    message_list = message_list.filter(course_id=course_id)
  if client_id:
    comment_list = comment_list.filter(author_id=client_id)
    message_list = message_list.filter(author_id=client_id)
  message_list = message_list.order_by("-time")
  message_query = []
  comment_query = []
  for message in message_list:
    message_id = message.id
    course = message.course
    c_id = course.course_id
    message_query.append({
      "id":message_id,
      "courseId": c_id,
      "userId": message.author_id,
      "userName": message.author.alias,
      "phoneNumber": message.author.id,
      "msgContent": message.content,
      "createdAt": str(message.time)
    })
    comment_list = Comment.objects.filter(message=message).order_by("-time")
    for comment in comment_list:
      course_query.append({
        "id": comment.id,
        "courseId": c_id,
        "userId": comment.author_id,
        "userName": comment.author.alias,
        "phoneNumber": comment.author.id,
        "msgContent": comment.content,
        "createdAt": str(comment.time)
      })
  query = __querysort__(message_query, comment_query)
  query = [{
    "id": "comment.id",
    "courseId": "c_id",
    "userId": "comment.author_id",
    "userName": "comment.author.alias",
    "phoneNumber": "comment.author.id",
    "msgContent": "comment.content",
    "createdAt": "str(comment.time)"
  }]
  return HttpResponse(json.dumps({"query": query}))

def delete_msg(request):
  msg_id = request.POST.get("msgId")
  msg_id = int(msg_id)
  status = 0
  try:
    msg = Message.objects.get(id=msg_id)
    msg.delete()
    record(request.user.id, 5, msg_id)
  except Message.DoesNotExist as e:
    status = 1
  return HttpResponse(json.dumps({"status": status}))
