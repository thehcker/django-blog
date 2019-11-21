from django.shortcuts import render
# from django.http import HttpResponse
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
		'posts': posts
	}
	return render(request, 'index.html', context)
	
def about(request):
	context = {
		'title': 'About Us'
	}
	return render(request, 'about.html', context)