import json
from django.http import JsonResponse
from backend.models import VisitRecord, User, AdminOperationRecord, Operation


def client_history(request):
    """

    A method to show clients' visiting history.

    Parameter is course_id that you want to search, which can be omitted.

    Output is an iterable list named history consisted of dict with three keys:
    course_id, user_id and last_visit.

    PS: The output last_visit is of Unix timestamp.

    """
    course_id = request.POST.get("course_id")
    record = VisitRecord.objects.filter()
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
    return JsonResponse({"history": history})


def client_information(request):
    user_id = request.POST.get("user_id")
    print(type(user_id))
    print(user_id)
    user_alias = request.POST.get("user_alias")
    user_list = None
    if user_id:
        user_list = User.objects.filter(id=user_id)
        if user_alias:
            user_list = user_list.filter(alias=user_alias)
    else:
        if user_alias:
            user_list = User.objects.filter(alias=user_alias)
    if user_list is None:
        user_list = User.objects.filter()
    user_list = user_list.values()
    query = []
    for client in user_list:
        query.append({
            "userId": client["id"],
            "userAlias": client["alias"],
            "bonus": str(client["balance"]),
            "is_V": client["is_V"]
        })
    if not query:
        query.append({
            "usreId": " ",
            "userAlias": " ",
            "bonus": " ",
        })
    return JsonResponse({"query": query})


def delete(request):
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        user.is_acitve = False
        user.save()
    except User.DoesNotExist:
        status = 1

    log_user_id = request.user.id
    log_object_id = user_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=3),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def ban(request):
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        user.talking_allowed = False
        user.save()
    except User.DoesNotExist:
        status = 1

    log_user_id = request.user.id
    log_object_id = user_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=4),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def authorize(request):
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        auth = json.loads(request.POST.get("auth"))
        user.is_V = auth
        user.save()
    except User.DoesNotExist:
        status = 1

    log_user_id = request.user.id
    log_object_id = user_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=5),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})
