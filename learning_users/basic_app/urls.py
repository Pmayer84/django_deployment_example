from django.contrib import admin
from django.urls import path, re_path
from basic_app import views
from django.conf.urls import include


app_name = 'basic_app'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login')
]