from django.conf.urls import patterns, include, url
from django.contrib import admin
from BOOKMS.views import hello
from BOOKMS.views import login
from BOOKMS.views import booklist
from BOOKMS.views import register
from BOOKMS.views import search
from BOOKMS.views import weibo
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
    url(r'^css/(?P<path>.*)', 'django.views.static.serve',{'document_root': settings.CSS_DIR}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^login/', login),
    url(r'^booklist/$', booklist),
    url(r'^register/', register),
    url(r'^search/', search),
    url(r'^weibo/', weibo),
)
