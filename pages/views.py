from django.shortcuts import render

# pages/views.py
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Page


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'
