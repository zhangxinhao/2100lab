from django.http import JsonResponse
from backend.models import VisitRecord, User, AdminOperationRecord, Operation


def client_history(request):
    """

    A method to show clients' visiting history.


    Parameter is a HTTP request:

    - `course_id`: can be omitted.


    Return is a HTTP JSON response:

    - `history`: an iterable list

    Sample:

    history = {
        "course_id": "123414",
        "user_id": "234525",
        "alias": "name",
        "last_visit": "1553453663"
    }

    """
    course_id = request.POST.get("course_id")
    record = VisitRecord.objects.filter()
    if course_id:
        record = record.filter(course_id=course_id)
    record = record.order_by("-last_time")
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
    """

    A method to get client information


    Params is a HTTP request:

    - `user_id`

    - `user_alias`


    Return is a HTTP JSON response:

    - `query`: a list

    Sample:

    query = [{
        "userId": "123441",
        "userAlias": "alias"
        "bonus": "2.52",
        "isV": True
    }]

    """
    user_id = request.POST.get("user_id")
    user_alias = request.POST.get("user_alias")
    user_list = None
    if user_id:
        user_list = User.objects.filter(id=user_id, is_active=True)
        if user_alias:
            user_list = user_list.filter(alias=user_alias)
    else:
        if user_alias:
            user_list = User.objects.filter(alias=user_alias, is_active=True)
    if user_list is None:
        user_list = User.objects.filter(is_active=True)
    user_list = user_list.values()
    query = []
    for client in user_list:
        query.append({
            "userId": client["id"],
            "userAlias": client["alias"],
            "bonus": str(client["balance"]),
            "isV": client["is_V"]
        })
    return JsonResponse({"query": query})


def delete(request):
    """

    A method to delete user.


    Param is a HTTP request:

    - `user_id`


    Returnis a HTTP JSON request

    - `status`: 0 means succeeded, 1 means failed

    """
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        user.is_active = False
        user.save()
        log_user_id = request.user.id
        log_object_id = user_id
        log = AdminOperationRecord.objects.create(
            admin_id=log_user_id,
            operation=Operation.objects.get(pk=3),
            object=log_object_id
        )
        log.save()
    except User.DoesNotExist:
        status = 1
    return JsonResponse({"status": status})


def ban(request):
    """

    Parameter is a HTTP `reuqest`:

    - `user_id`


    Return:

    - `status`: 0 means succeeded, 1 means failed

    """
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        user.talking_allowed = False
        user.save()
    except User.DoesNotExist:
        status = 1
        return JsonResponse({"status": status})

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
    """

    A method to authorize user


    Param is a HTTP request

    - `user_id`

    Return:

    - `status`: 0 means succeeded, 1 means failed

    """
    status = 0
    user_id = request.POST.get("user_id")
    try:
        user = User.objects.get(id=user_id)
        user.is_V = True
        user.save()
    except User.DoesNotExist:
        status = 1
        return JsonResponse({"status": status})

    log_user_id = request.user.id
    log_object_id = user_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=5),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})
