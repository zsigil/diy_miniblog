from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as account_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', account_views.SignUpView, name='signup'),
    path('createauthor/', account_views.AuthorCreateView, name='create_author'),
]
