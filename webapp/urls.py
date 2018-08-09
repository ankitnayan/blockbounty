from . import views
from django.conf.urls import include, url

urlpatterns = [
    url('team', views.team, name='team'),
    url('', views.index, name='index'),
]