from .manager import client, admin_views, msg_mng
from django.conf.urls import url, include
from . import views, user_views, order_views, course_views, pay
from django.urls import path


urlpatterns = [
  path('', views.index),
  path('login/', user_views.login),
  path('authenticate/', user_views.authenticate),
  path('logout/', user_views.logout),
  path('listrecentvisit/', user_views.listRecentVisit),
  path('getuserinfo/', user_views.getUserInfor),
  path('getcourseinfo/', course_views.getCourseInfo),
  path('setalias/', user_views.setAlias),
  path('seticon/', user_views.setIcon),
  path('setuserdata/', user_views.setUserData),
  path('listrecommend/', views.recommendCourse),
  path('listfreeindex/', views.briefFreeCourses),
  path('listpricedindex/', views.briefPricedCourses),
  path('listfreecourses/', views.freeCourses),
  path('listpricedcourses/', views.pricedCourses),
  path('listorders/', order_views.getOrders),
  path('getcode/',user_views.getCode),
  path('coursepage/', course_views.loadCourse),
  path('admin_userhistory/', client.client_history),
  path('paywithqr/', pay.pay_qr),
  path('clientinfor/', client.client_information),
  path('deleteclient/', client.delete),
  path('banclient/', client.ban),
  path('adminlogin/', admin_views.authenticate),
  path('adminlogout/', admin_views.logout),
  path('authorizationcheck/', admin_views.authorization_check),
  path('showmessage/', msg_mng.show_msg),
  path('deletemsg/', msg_mng.delete_msg),
  path('shutup/', admin_views.ban_client),
]
