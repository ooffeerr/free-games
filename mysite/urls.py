from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       #url(r'^snippets/', include('snippets.urls')),
                       url(r'^free_games/', include('free_games.urls', namespace="free_games")),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
