from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('post/create',views.create,name='create'),
path('post/editPost/<id>',views.edit,name='editPost'),
path('',views.show,name='posts'),
path('post/<id>',views.details,name='post'),
path('post/delete/<id>',views.delete,name='delete'),

]   