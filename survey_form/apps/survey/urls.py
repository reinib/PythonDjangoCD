from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey/result$', views.result),
    url(r'^destroy_everything$', views.back)
]
