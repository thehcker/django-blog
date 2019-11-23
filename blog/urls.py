from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

app_name = 'blog'

urlpatterns = [
	# path('', views.home, name='home'),
	path('', PostListView.as_view(template_name='index.html'), name='index'),
	path('post/create', PostCreateView.as_view(template_name='post_create.html'), name='post_create'),
	path('post/<int:pk>', PostDetailView.as_view(template_name='post_detail.html'), name='post_detail'),
	path('post/<int:pk>/update', PostUpdateView.as_view(template_name='post_update.html'), name='post_update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post_delete'),
	path('about/', views.about, name='about'),
]