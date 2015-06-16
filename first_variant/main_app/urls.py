from django.conf.urls  import patterns, include, url
#import django.conf.url
urlpatterns = patterns('',
	url(r'^1', 'main_app.views.basic'),
  url(r'^post','main_app.views.testgraphic')


	)