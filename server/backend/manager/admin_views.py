from django.contrib import auth
from django.http import JsonResponse
from backend.models import User, RightsList, AdminOperationRecord, Operation



def authenticate(request):
    """

    A function to login for administrators.

    Parameters:

    - A HTTP `request`

        - `username`

        - `password`

    Returns:

    - `status`: 0 means login and 1 means failure

    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)
    status = 0
    if not user:
        status = 1
    elif user.is_staff:
        auth.login(request, user)
    else:
        status = 1
    return JsonResponse({"status": status})


def logout(request):
    """

    A function to logout

    Param: A HTTP `request`

    """
    auth.logout(request)
    return JsonResponse({"status": 0})


def _to_binary_(code):

    """
    An inner function to turn a integer into 5 bit binary(a string)


    Parameter:

    - `code`: integer


    Return:

    - A 5 bit binary string

    """
    my_str = bin(code)
    my_str = my_str[2:]
    size = len(my_str)
    delta = '0' * (5 - size)
    return delta + my_str


def access_check(request):
    """

    A function to check access before someone enter a admin page.


    Parameter:

    - A HTTP `request`


    Return:

    - A HTTP json response

        - `status`: 0 means admin, 1 means he is not admin

        - `code`: a 5 bit binary string representing his limit of authentication

    """
    status = 0
    user = request.user
    code = ""
    if user.is_authenticated and user.is_staff:
        code = _to_binary_(user.manage_right)
    else:
        status = 1
    return JsonResponse({"status": status, "code": code})


def authorization_check(request):
    """

    A function to check what kind of authentication an admin has.


    Parameter:

    - A HTTP `request`


    Return:

    - `rights`: A dict with 5 key pairs in it.

    Sample:

    rights = {

        "courseManage": False,

        "userManage": False,

        "operationHistory": False,

        "orderManage": False,

        "adminManage": False
    }

    """
    user = request.user
    my_list = _to_binary_(user.manage_right)
    rights = {}
    for i in range(len(my_list)):
        try:
            right = RightsList.objects.get(id=i).right
            if my_list[i] == '1':
                rights[right] = True
            else:
                rights[right] = False
        except RightsList.DoesNotExist:
            rights = {
                "courseManage": False,
                "userManage": False,
                "operationHistory": False,
                "orderManage": False,
                "adminManage": False
            }
    return JsonResponse({"rights": rights})


def ban_client(request):
    """

    A method to ban a client to post.


    Parameter:

    - A HTTP `reuqest`

    Return:

    - `status`: 0 means succeeded, 1 means failed

    """
    client_id = request.POST.get("userId")
    status = 0
    try:
        user = User.objects.get(id=client_id)
        if user:
            user.cannot_talk()
        else:
            status = 1
    except User.DoesNotExist:
        status = 1
        return JsonResponse({"status": status})

    log_user_id = request.user.id
    log_object_id = client_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=4),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def create_admin(request):
    """

    A super administrator's method


    Parameter:

    - A HTTP `request` using POST

        - `adminName`: the admin's id and username

        - `password`: the password

        - `right`: a dict to record admin's limit of authentication


    Sample:

    right = {

        "courseManage": "false",

        "userManage": "false",

        "operationHistory": "false",

        "orderManage": "false",

        "adminManage": "true"
    }


    Return:

    - `status`: 0 means succeeded, 1 means username is occupied

    """
    status = 0
    user_name = request.POST.get("adminName")
    try:
        user = User.objects.filter(id=user_name)
        if user:
            status = 1
            return JsonResponse({"status": status})
    except User.DoesNotExist:
        status = 0
    rights_code = ['0', '0', '0', '0', '0']
    right_list = RightsList.objects.filter().values()
    for right in right_list:
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
        manage_right=right
    )
    user.save()

    log_user_id = request.user.id
    log_object_id = user_name
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=8),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def get_admin(request):
    """

    A method to get admin's limit of authentication


    Parameters:

    - A HTTP `request`

        - `adminId`


    Return is a HTTP response:

    - `status`: 0 means succeeded, 1 means failed

    - `admins`: A dict

    admins = {
        "adminId": "12334",

        "password": "",

        "courseManage": False,

        "userManage": False,

        "operationHistory": False,

        "orderManage": False,

        "adminManage": True
    }

    """
    admin_id = request.POST.get("adminId")
    user_list = None
    admins = []
    status = 0
    if admin_id:
        try:
            user = User.objects.get(pk=admin_id)
            right = _to_binary_(user.manage_right)
            admin = {"adminId": admin_id, "password": ''}
            for i in range(len(right)):
                rght = RightsList.objects.get(id=i).right
                if right[i] == '1':
                    admin[rght] = True
                else:
                    admin[rght] = False
            admins.append(admin)
        except User.DoesNotExist:
            status = 1
    else:
        user_list = User.objects.filter(is_staff=True).order_by("id").values()
        for admin in user_list:
            the_one = {
                "adminId": admin["id"], "password": ''}
            right = _to_binary_(admin["manage_right"])
            try:
                for i in range(len(right)):
                    rght = RightsList.objects.get(id=i).right
                    if right[i] == '1':
                        the_one[rght] = True
                    else:
                        the_one[rght] = False
                admins.append(the_one)
            except RightsList.DoesNotExist:
                status = 1
    return JsonResponse({"status": status, "admins": admins})


def edit_admin(request):
    """

    A method to edit admin's information


    Params is a HTTP request

    - `adminId`

    - 'courseManage'

    - 'userManage'

    - 'operationHistory'

    - 'orderManage'

    - 'adminManage'


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed

    """
    status = 0
    admin_id = request.POST.get("adminId")
    admin = User.objects.get(id=admin_id)
    if admin:
        rights_code = ['0', '0', '0', '0', '0']
        right_list = RightsList.objects.filter().values()
        for right in right_list:
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
        return JsonResponse({"status": status})

    log_user_id = request.user.id
    log_object_id = admin_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=9),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def delete_admin(request):
    """

    A method to delete an admin


    Param is a HTTP request:

    - `adminId`


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed

    """
    status = 0
    admin_id = request.POST.get("adminId")
    admin = User.objects.get(id=admin_id)
    if admin:
        admin.set_active()
    else:
        status = 1

    log_user_id = request.user.id
    log_object_id = admin_id
    log = AdminOperationRecord.objects.create(
        admin_id=log_user_id,
        operation=Operation.objects.get(pk=10),
        object=log_object_id
    )
    log.save()
    return JsonResponse({"status": status})


def record_list(request):
    """

    A method to return the list of record of admins' operation.


    Param is a HTTP request:

    - `adminId`: can be None

    - `objectId`: can be None

    Pay attention: the two query condition will search in the same time. `None`
    means the item will search all.


    Return is a HTTP JSON response:

    - `status`: 0 means succeeded, 1 means failed

    - `history`: a list of dict

        Sample:

        history = [{

            "adminId": data.admin_id,

            "operation": data.operation.operation,

            "objectId": data.object,

            "time": "2018-02-03 12:23:12"
        }]

    """
    status = 0
    admin_id = request.POST.get("adminId")
    object_id = request.POST.get("objectId")
    record = None
    if admin_id:
        record = AdminOperationRecord.objects.filter(admin_id=admin_id)
        if object_id:
            record = record.filter(object=object_id)
    elif object_id:
        record = AdminOperationRecord.objects.filter(object=object_id)
    else:
        record = AdminOperationRecord.objects.filter().order_by("-time")
    history = []
    for data in record:
        try:
            history.append({
                "adminId": data.admin_id,
                "operation": data.operation.operation,
                "objectId": data.object,
                "time": data.time.strftime('%Y-%m-%d %H:%M:%S')
            })
        except Operation.DoesNotExist:
            status = 1
    return JsonResponse({"status": status, "history": history})
