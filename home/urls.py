from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Only this for root
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('login-or-register/', views.login_or_register, name='login_or_register'),
    path('register/', views.user_register, name='register'),
    # ...other urls...
]