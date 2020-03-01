from django.shortcuts import render

# pages/views.py
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'object_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'


class PageCreateView(CreateView):
    model = Page
    template_name = 'page_new.html'
    fields = '__all__'


class PageUpdateView(UpdateView):
    model = Page
    template_name = 'page_edit.html'
    fields = ['title', 'body']


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'page_delete.html'
    success_url = reverse_lazy('home')
