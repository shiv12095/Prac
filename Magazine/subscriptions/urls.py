from django.conf.urls import patterns, url
from subscriptions import views

urlpatterns = patterns('',
	url(r'^$' , views.index , name='index'),
	url(r'^new' , views.new , name='new'),
	url(r'^view/(?P<subscription_id>[\w\-]+)/$' , views.view , name='view'),
	url(r'^edit/(?P<subscription_id>[\w\-]+)/$' , views.edit , name='edit'),
	url(r'^cancel/(?P<subscription_id>[\w\-]+)/$' , views.cancel , name='cancel'),
	url(r'^expiring' , views.expiring , name='expiring'),
	url(r'^cancelled' , views.cancelled , name='cancelled'),
	)