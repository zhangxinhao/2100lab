from django.http import HttpResponse
from .models import User
import json

# def authenticate(request):
#   phone_number = request.POST.get('phone_number')
#   verification_code = request.POST.get('verification_code')
#   if(not verification_code):
#     user =

def login(request):
  if request.user.is_authenticated:
    return HttpResponse(json.dumps({"status": True,"user": request.user}))
  else:
    return HttpResponse(json.dumps({"status": False}))
