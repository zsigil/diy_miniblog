from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blogs/', views.AllBlogsView.as_view(), name='all_blogs'),

    path('<int:pk>/createcomment/', views.CommentCreateView, name='create_comment'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),

    path('bloggers/', views.AllBloggersView.as_view(), name='all_bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger_detail'),



]
