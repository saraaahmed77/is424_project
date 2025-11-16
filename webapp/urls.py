from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Index / home
    path('', views.Welcome, name='welcome'),

    path('register/', views.register_view, name='register'),

    # URL login
    path('login/', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),

    path('product/', views.product, name='product'),

    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('basket/', views.basket, name='basket'),
    path('basket/add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),

]
