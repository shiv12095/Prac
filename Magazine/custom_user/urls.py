from django.conf.urls import patterns, url
from custom_user import views

urlpatterns = patterns('',
		url(r'^$' , views.login , name='index'),
		url(r'^index', views.index, name='index'),
		url(r'^signup', views.signup, name='signup'),
		url(r'^login', views.login, name='login'),
		url(r'^logout', views.logout, name='logout'),		
		url(r'^profile', views.profile, name='profile'),
	)