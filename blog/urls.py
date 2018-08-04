from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('problem/', views.ProblemView.as_view(), name='problem'),

    path('blogs/', views.AllBlogsView.as_view(), name='all_blogs'),

    path('<int:pk>/createcomment/', views.CommentCreateView, name='create_comment'),
    path('<int:blogid>/comments/<int:commentid>/update/', views.CommentUpdateView,name='update_comment'),
    path('<int:blogid>/comments/<int:commentid>/delete/', views.CommentDeleteView,name='delete_comment'),

    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),

    path('bloggers/', views.AllBloggersView.as_view(), name='all_bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger_detail'),



]
