
#menu/urls.py
from django.urls import path

from. import views

urlpatterns=[
	#Empty or blank url
	#localhost:8000/
	path('',views.homemenu,name='myhome'),
	path('about/',views.aboutmenu,name='about'),
	path('login/',views.loginmenu,name='mylogin'),
	path('registration/',views.registration,name='registration'),
	path('logout/',views.logout,name='logoutURL'),

]
