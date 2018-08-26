from django.http import JsonResponse
from .models import User

PERCENTAGE = 0.05


def distribute(request):
    """

    A method to distribute bonus while a user-shared course was bought.

    Parameters:
    sharer_id, None or it's id; price, with the unit yuan.

    Output:
    status and result.
    If status is 0, the result will be "Distributed" no matter the input parameter
    sharer_id is None or the sharer actually get his bonus.
    If status is 1, the result wiil be "User inexistent", which means the sharer_id is inexistent.

    """
    sharer_id = request.POST.get("sharer_id")
    if sharer_id:
        sharer = User.objects.get(id=sharer_id)
        if not sharer:
            return JsonResponse({"status": 1, "result": "User inexistent"})
        price = request.POST.get("price")
        bonus = __get_bonus__(price)
        sharer.balance = sharer.balance + bonus
    return JsonResponse({"status": 0, "result": "Distributed"})


def __get_bonus__(price):
    """

    An inner method to return a number with at most 2 decimal fractions.

    """
    bonus = price * 0.05
    bonus = bonus * 100
    bonus_str = str(bonus)
    if "." in bonus_str:
        bonus_split = bonus_str.split(".")
        bonus = int(bonus_split[0])
        if bonus_split[1][0] > '4':
            bonus = bonus + 1
    return bonus / 100
