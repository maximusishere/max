from django.urls import path
from blog.views import index, category_posts, post_detail
from .views import PostCreateView, ProfileDetailView, ProfileUpdateView, PostDetailView, PostUpdateView


app_name = 'blog'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('posts/<str:author_id>/<int:id>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path(
        'profile/<slug:author_id>/', ProfileDetailView.as_view(), name='profile'
    ),
    path(
        'profile/<str:username>/edit/',
        ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    path('posts/<str:author_id>/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('posts/<int:id>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_posts, name='category_posts'),
    path('', index, name='index'),
]
