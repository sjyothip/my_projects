from django.urls import path
from my_app import views

urlpatterns = [
	
	path('log_usr',views.log_usr,name='log_usr'),

	path('log',views.log,name='log'),
	
	path('main',views.main,name='main'),

	path('testview',views.testview,name='testview'),

	path('usr_pst',views.usr_pst,name='usr_pst'),

	path('test_ing',views.test_ing,name='test_ing'),

	path('mock_time_limit',views.mock_time_limit,name='mock_time_limit'),

	path('testhtml',views.testhtml,name='testhtml'),

	path('testhtml2',views.testhtml2,name='testhtml2'),

	path('usr_del',views.usr_del,name='usr_del'),

	path('usr_get_msgs',views.usr_get_msgs,name='usr_get_msgs'),

	path('usr_pst_msgs',views.usr_pst_msgs,name='usr_pst_msgs'),

	path('messagehtml',views.messagehtml,name='messagehtml'),

	path('chats',views.chats,name='chats'),

	path('usr_chat',views.usr_chat,name='usr_chat'),

	path('chat_del',views.chat_del,name='chat_del'),

	path('logout_request',views.logout_request,name='logout_request'),

	path('test_test',views.test_test,name='test_test'),

	# path('testhtml',views.testhtml,name='testhtml'),

	# path('testhtml',views.testhtml,name='testhtml'),

	# path('testhtml',views.testhtml,name='testhtml'),

	# path('testhtml',views.testhtml,name='testhtml'),

	# path('testhtml',views.testhtml,name='testhtml'),
	

]

