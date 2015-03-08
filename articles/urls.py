from django.conf.urls import patterns, include, url

from articles import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	# url(r'^display=(?P<num_to_display>\d+)/$', views.display, name="display"),
	url(r'^change_display/$', views.change_display, name="change_display"),
	url(r'^(?P<article_id>\d+)/$', views.articleid, name="articleid"),
	url(r'^(?P<dep>[A-Z]+)/$', views.department, name="department"),
)