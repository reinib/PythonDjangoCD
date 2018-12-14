from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy$', views.buy),
    url(r'^purchase$', views.purchase),
    # url(r'^remove$', views.remove),
    # url(r'^delete$', views.delete),
]
