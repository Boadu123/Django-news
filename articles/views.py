from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy

from .models import Article

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'registration/article_list.html'
    
class ArticleDetailView(LoginRequiredMixin, DetailView): # new
    model = Article
    template_name = 'registration/article_detail.html'
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'registration/article_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'registration/article_delete.html'
    success_url = reverse_lazy('registration/article_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'registration/article_new.html'
    fields = ('title', 'body',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)