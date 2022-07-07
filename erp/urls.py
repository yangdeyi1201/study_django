"""
============================
Author:杨德义
============================
"""
from django.urls import path, re_path
from . import views

app_name = 'erp'

urlpatterns = [
    path('api', views.api, name='api')
]
