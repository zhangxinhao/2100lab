from django.http import JsonResponse
from .models import Course, Message, Comment, Attitude


def message_board_dic(request):
    """

    An inner method, which shoud not be called directly by the frontend.
    The returned value is dict-typed and serializable.
    It contains all information of a message board that you may use.

    """
    course = Course.objects.get(pk=request.POST.get("course_id"))
    message = Message.objects.filter(course=course).order_by("-time")
    messages = []
    for msg in message:
        user = msg.author
        comments = Comment.objects.filter(message=msg)
        reply = []
        for cmt in comments:
            reply.append({
                "userName": cmt.author.alias,
                "userType": cmt.author.is_V,
                "indisMessage": cmt.content
            })
        messages.append({
            "message_id": msg.id,
            "author": user.alias,
            "icon": user.icon.name,
            "content": msg.content,
            "time": msg.time.strftime('%Y-%m-%d %H:%M:%S'),
            "likes": msg.likes,
            "dislikes": msg.dislikes,
            "reply": reply,
            "usertype": user.is_V
        })
    return messages


def message_board(request):
    """

    Call this method directly to return a serialized value in Json.

    """
    return JsonResponse(message_board_dic(request))


def leave_message(request):
    """

    A method to leave message. Course id and the message itself are needed.

    """
    user = request.user
    if not user.talking_allowed:
        status = 1
        return JsonResponse({"status": status})
    course_id = request.POST.get("course_id")
    content = request.POST.get("content")
    course = Course.objects.get(pk=course_id)
    Message.objects.create(course=course, author=user,
                           content=content)
    response = {}
    my_message_board = message_board_dic(request)
    if my_message_board:
        response["message"] = my_message_board
    return JsonResponse(response)


def comment(request):
    """

    A method to make comment. Message id, to which this comment belongs, is needed.

    """
    user = request.user
    if not user.talking_allowed:
        status = 1
        return JsonResponse({"status": status})
    message_id = request.POST.get("message_id")
    content = request.POST.get("content")
    message = Message.objects.get(pk=message_id)
    Comment.objects.create(author=user, message=message, content=content)
    response = {}
    my_message_board = message_board_dic(request)
    if my_message_board:
        response["message"] = my_message_board
    return JsonResponse(response)


def express(request):
    """

    Using this method to express you like or dislike.
    It need a parameter named attitude.
    "like" means like and same to dislike.

    """
    user = request.user
    choice = False
    if request.POST.get("attitude") == "like":
        choice = True
    message_id = request.POST.get("message_id")
    delta = 0
    message = Message.objects.get(pk=message_id)
    done = Attitude.objects.filter(user=user, message=message, like=choice)
    if not done:
        Attitude.objects.create(user=user, message=message, like=choice)
        delta = 1
    else:
        delta = -1
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
    response = {}
    my_message_board = message_board_dic(request)
    if my_message_board:
        response["message"] = my_message_board
    return JsonResponse(response)
