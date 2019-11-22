from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
	{
		'author': 'Isaac Nyakoi',
		'title': 'Blog Post 1',
		'content': 'First Post content',
		'date': 'Twentieth November 2019'
	},
	{
		'author': 'Alicia Keys',
		'title': 'Blog Post 2',
		'content': 'Second Post content',
		'date': 'Twentieth November 2019'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'index.html', context)
	
def about(request):
	context = {
		'title': 'About Us'
	}
	return render(request, 'about.html', context)