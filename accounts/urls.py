from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

path('register/',views.register),
path('login/',views.log_in,name='login'),
path('logout/',views.log_out,name='logout')


]