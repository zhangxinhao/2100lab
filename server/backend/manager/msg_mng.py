from django.http import JsonResponse
from backend.models import Message, Comment, AdminOperationRecord, Operation
from datetime import timedelta, timezone


def _querysort_(message, comment):
    message.extend(comment)
    return message


def show_msg(request):
    """

    A method to show messages and replys.


    Param is a HTTP POST request:

    - `course_id`: can be None and will return all

    - `client_id`: can be None and will return all


    Return is a HTTP JSON response:

    - `query`: a list of courses, each course is in a dict


    """
    course_id = request.POST.get("courseId")
    client_id = request.POST.get("clientId")
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
    course_query = []
    for message in message_list:
        message_id = message.id
        course = message.course
        c_id = course.course_id
        message_query.append({
            "id": message_id, "courseId": c_id, "userId": message.author_id,
            "msgContent": message.content, "createdAt": str(message.time),
            "userName": message.author.alias,
            "phoneNumber": message.author.id
        })
        comment_list = Comment.objects.filter(
            message=message).order_by("-time")
        for comment in comment_list:
            course_query.append({
                "id": comment.id, "courseId": c_id,
                "userId": comment.author_id,
                "userName": comment.author.alias,
                "phoneNumber": comment.author.id,
                "msgContent": comment.content,
                "createdAt": str(comment.time)
            })
    query = _querysort_(message_query, comment_query)
    return JsonResponse({"query": query})


def delete_msg(request):
    """

    A method to soft delete message.


    Param is a HTTP POST request:

    - `msgId`


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed
    """
    msg_id = request.POST.get("msgId")
    msg_id = int(msg_id)
    status = 0
    try:
        msg = Message.objects.get(id=msg_id)
        if msg:
            msg.delete()
        else:
            status = 1
    except Message.DoesNotExist:
        status = 1

    log_user_id = request.user.id
    log_object_id = msg_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=6),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})
