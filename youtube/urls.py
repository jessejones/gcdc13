from django.conf.urls import patterns, url
from youtube import views

urlpatterns = patterns('',
    url(r'^search(?P<mid>/m/\w+)/$', views.display_results, name='results'),
)