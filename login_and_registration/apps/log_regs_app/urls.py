from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate_register$', views.validate_register),
    url(r'^users/(?P<id>\d+)$', views.success),
    url(r'^validate_login$', views.validate_login),
]
