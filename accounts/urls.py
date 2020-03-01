#!/usr/bin/env python3
# coding: utf-8

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]