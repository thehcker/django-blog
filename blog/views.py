from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
									DetailView, 
									CreateView, 
									UpdateView,
									DeleteView
									)
from .models import Post
# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'index.html', context)

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	# success_url = '/'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Post
	# success_url = '/'
	fields = ['title', 'content']

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
def about(request):
	context = {
		'title': 'About Us'
	}
	return render(request, 'about.html', context)