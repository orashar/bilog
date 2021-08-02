from django.contrib import admin
from django.urls import path, include

from .views import (
    HomeView, 
    ArticleDetailView,
    AddPostView,
    AddCategoryView,
    UpdatePostView,
    DeletePostView,
    CategoryView,
    CategoryListView,
    LikeView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:catg>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like-post'),
]
