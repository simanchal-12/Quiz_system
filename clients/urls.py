
#menu/urls.py
from django.urls import path

from. import views

urlpatterns=[

		path('',views.clientListing,name='clientListing'),
	

]
