from django.conf.urls import url, include
from . import views, user_views, order_views
from django.urls import path

urlpatterns = [
  path('', views.index),
  path('authenticate/', user_views.authenticate),
  path('logout/', user_views.logout),
  path('listrecentvisit/', user_views.listRecentVisit),
  path('getuserinfo/', user_views.getUserInfor),
  path('setalias/', user_views.setAlias),
  path('seticon/', user_views.setIcon),
  path('listrecommend/', views.recommendCourse),
  path('listfreeindex/', views.briefFreeCourses),
  path('listpricedindex/', views.briefPricedCourses),
  path('listfreecourses/', views.freeCourses),
  path('listpricedcourses/', views.pricedCourses),
  path('listorders/', order_views.getOrders),
  path('getcode/',user_views.getCode),
]
