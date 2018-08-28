from django.urls import path
from .manager import admin_views, client, course_mng_views, msg_mng
from .manager import orders_views
from . import views, user_views, order_views, course_views, message_views, pay


urlpatterns = [
    path('', views.index),
    path('login/', user_views.login),
    path('authenticate/', user_views.authenticate),
    path('logout/', user_views.logout),
    path('listrecentvisit/', user_views.get_visit_history),
    path('getuserinfo/', user_views.get_user_infor),
    path('getcourseinfo/', course_views.get_course_info),
    path('setalias/', user_views.set_alias),
    path('seticon/', user_views.set_icon),
    path('setuserdata/', user_views.set_user_data),
    path('listrecommend/', views.recommend_course),
    path('listfreeindex/', views.brief_free_courses),
    path('listpricedindex/', views.brief_priced_courses),
    path('listfreecourses/', views.free_courses),
    path('listpricedcourses/', views.priced_courses),
    path('listorders/', order_views.get_orders),
    path('getcode/', user_views.get_code),
    path('coursepage/', course_views.load_course),
    path('admin_userhistory/', client.client_history),
    path('clientinfor/', client.client_information),
    path('deleteclient/', client.delete),
    path('banclient/', client.ban),
    path('adminlogin/', admin_views.authenticate),
    path('adminlogout/', admin_views.logout),
    path('authorizationcheck/', admin_views.authorization_check),
    path('showmessage/', msg_mng.show_msg),
    path('deletemsg/', msg_mng.delete_msg),
    path('shutup/', admin_views.ban_client),
    path('manageorder/', orders_views.list_order),
    path('createadmin/', admin_views.create_admin),
    path('getadmin/', admin_views.get_admin),
    path('editadmin/', admin_views.edit_admin),
    path('deleteadmin/', admin_views.delete_admin),
    path('getpv/', orders_views.get_pv),
    path('getvol/', orders_views.get_vol),
    path('recordlist/', admin_views.record_list),
    path('showcourse/', course_mng_views.show_courses),
    path('uploadaudio/', course_mng_views.upload_audio),
    path('uploadcourse/', course_mng_views.upload_course),
    path('uploadcoursepicture/', course_mng_views.upload_course_picture),
    path('authorize/', client.authorize),
    path('leaveMessage/', message_views.leave_message),
    path('comment/', message_views.comment),
    path('attitude/', message_views.express),
    path('chargewebhooks/', pay.webhooks_charge),
    path('refundwebhooks/', pay.webhooks_refund),
    path('feedbackrecord/', course_views.feedback_course_record),
    path('checkrecord/', course_views.check_course_record),
    path('alipaypc/', pay.alipay_pc),
    path('alipayphone/', pay.alipay_phone),
    path('wxpc/', pay.wx_pc),
    path('wxphone/', pay.wx_phone),
    path('refund/', orders_views.refund),
    path('preload/', course_mng_views.preload_course),
    path('editcourse/', course_mng_views.edit_course),
    path('accesscheck/', admin_views.access_check),
    path('bonuspay/', pay.bonus_pay),


]
