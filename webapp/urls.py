from . import views
from django.conf.urls import include, url

urlpatterns = [
    url('about', views.about, name='about'),
    url('', views.index, name='index'),
]