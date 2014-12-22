from django.conf.urls import patterns, url

from free_games import views

urlpatterns = patterns('',
     # ex: /free_games/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /free_games/<game_id>/detail
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)