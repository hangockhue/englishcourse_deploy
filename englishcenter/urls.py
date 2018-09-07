#!/usr/bin/python

# -*- coding: utf8 -*-
from django.urls import path, include
from . import views

app_name = 'englishcourse'

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('register', views.register, name='register')
]