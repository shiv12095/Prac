from django.conf.urls import patterns, url
from subscriptions import views

urlpatterns = patterns('',
	url(r'^$' , views.index , name='index'),
	url(r'^new' , views.new , name='new'),
	url(r'^view/(?P<subscription_id>[\w\-]+)/$' , views.view , name='view'),
	url(r'^expiring' , views.expiring , name='expiring'),
	)