from django.urls import path
from .views import PostListCreateView, PostDetailView, CategoryListCreateView, TagListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post_list_create'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('tags/', TagListCreateView.as_view(), name='tag_list_create'),
]
