from django.conf.urls import url, include
from . import views, user_views
from django.urls import path

urlpatterns = [
  path('', views.index),
  path('authenticate/', user_views.authenticate),
  path('logout/', user_views.logout),
  path('listrecentvisit/', user_views.listRecentVisit),
]
