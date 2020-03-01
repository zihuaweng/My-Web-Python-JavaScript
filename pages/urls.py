#!/usr/bin/env python3
# coding: utf-8

# pages/urls.py
from django.urls import path
from .views import (HomePageView,
                    AboutPageView,
                    PageDetailView,
                    PageCreateView,
                    PageUpdateView,
                    PageDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('page/<int:pk>/edit', PageUpdateView.as_view(), name='page_edit'),
    path('page/<int:pk>/delete', PageDeleteView.as_view(), name='page_delete'),
    path('page/new', PageCreateView.as_view(), name='page_new')
]
