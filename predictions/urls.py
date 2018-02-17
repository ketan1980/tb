from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pred_list, name='pred_list'),
]
