from django.conf.urls import patterns, include, url
from app import views

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
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^youtube/', include('youtube.urls', namespace='youtube')),
)