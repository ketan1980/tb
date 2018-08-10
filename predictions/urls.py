from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pred_list, name='pred_list'),
    url(r'^spider/(?P<pk>.+?)/$', views.spider_chart, name='spider'),
    url(r'^player_stats/(?P<pk>.+?)/$', views.player_stats, name='player_stats'),
    url(r'^hhmatches/(?P<pk>.+?)/$', views.hhmatches, name='hhmatches'),
    url(r'^histrank/(?P<pk>.+?)/$', views.rankChart, name='rankChart'),
    url(r'^pastmatches/(?P<pk>.+?)/(?P<pl>.+?)/$', views.pastmatches, name='pastmatches'),
]
