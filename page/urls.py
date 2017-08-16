from django.conf.urls import patterns, url, include
from page import views

urlpatterns = patterns('',
                       url(r'^(?:(?P<category_id>\d+)/)?$', views.index, name='index'),
                       url(r'good/(?P<good_id>\d+)/$', views.good, name='good'),
                       )
