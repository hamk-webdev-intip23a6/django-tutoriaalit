from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Post

class PostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Post
    template_name = 'guestbook/post.html'
    fields = ['comment']
    success_url = reverse_lazy('guestbook:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

class PostListView(ListView):
    model = Post
    template_name = 'guestbook/index.html'
    context_object_name = 'posts'
    ordering = ['-date']
