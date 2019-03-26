from django.conf.urls import url
from fibonacci import views

urlpatterns = [
	url(r'^$', views.index,name="nth-positioned-fibonacci"),
	url(r'^get/nth-position-fibonacci$', views.getNthInstanceOfFibonacci, name="nth-positioned-fibonacci"),
    url(r'^get/nth-position-fibonacci/$', views.getNthInstanceOfFibonacci, name="nth-positioned-fibonacci"),
    url(r'^get/latest/searches/$', views.get_latest_searches, name="nth-positioned-fibonacci"),
]