from django.shortcuts import render

# pages/views.py
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from .models import Page


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'object_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'
