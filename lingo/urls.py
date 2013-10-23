from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from lingo import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lingoapp.views.home', name='home'),
    # url(r'^lingoapp/', include('lingoapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)