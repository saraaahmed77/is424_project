from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Index / home
    path('', views.index_view, name='index'),

    # URL login
    path('login', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),
    
    # URL sign up
    path('signup', views.signup_view, name='signup'),
]
