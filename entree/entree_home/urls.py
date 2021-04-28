from django.conf.urls import url
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^services$', services, name='services'),
    url(r'^login_home$', login_home, name='login_home'),
    url(r'^about_us', about_us, name='about_us'),
    url(r'^contact_us', contact_us, name='contact_us'),
    url(r'^get_in_touch', views.get_in_touch, name='get_in_touch'),

]