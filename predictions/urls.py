from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pred_list, name='pred_list'),
    url(r'^spider/(?P<pk>.+?)/$', views.spider_chart, name='spider'),
]
