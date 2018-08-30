import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Order, OrderStatus


def get_orders(request):
    """

    Output an iterable set, composed of dict.
    The keys' name of dict are: order_id, course_name, price, status and time.

    """
    try:
        user = request.user
        order_list = Order.objects.filter(user_id=user.id).order_by("-time")
        orders = []
        for item in order_list:
            order = {}
            order_id = item.order_id
            course = item.course
            course_name = course.course_name
            price = course.price
            status = item.status
            time = item.time
            order["order_id"] = order_id
            order["course_name"] = course_name
            order['course_id'] = course.id
            order["price"] = price
            order["status"] = OrderStatus.objects.get(status_code=status)
            order["time"] = time
            orders.append(order)
        return JsonResponse({"orders": json.loads(serialize("json", orders))})
    except (OrderStatus.DoesNotExist, AttributeError):
        return JsonResponse({"result": 1})
