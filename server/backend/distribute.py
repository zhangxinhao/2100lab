import math
from .models import Course, User

PERCENTAGE = 0.05


def distribute(sharer_id, course_id, price):
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
    status = 0
    try:
        sharer = User.objects.get(id=sharer_id)
        bonus = _get_bonus_(course_id, price)
        sharer.balance = sharer.balance + bonus
    except User.DoesNotExist:
        status = 1
    return status


def _get_bonus_(course_id, price):
    """

    An inner method to return a number with at most 2 decimal fractions.

    """
    try:
        course = Course.objects.get(course_id=course_id)
        bonus = price * course.percentage
        bonus = math.floor(bonus * 100)
        return bonus / 100
    except Course.DoesNotExist:
        return 0
