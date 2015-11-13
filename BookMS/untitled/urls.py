from django.conf.urls import patterns, include, url
from django.contrib import admin
from BOOKMS.views import hello
from BOOKMS.views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^login/', login),
)
