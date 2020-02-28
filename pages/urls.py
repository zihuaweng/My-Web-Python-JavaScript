#!/usr/bin/env python3
# coding: utf-8

# pages/urls.py
from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home')
]
