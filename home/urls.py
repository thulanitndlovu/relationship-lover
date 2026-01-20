from django.urls import path
from . import views

urlpatterns = [   
    path('', views.welcome, name='home') ,
    path("register/", views.user_register, name="register"),
    path("welcome/", views.welcome, name="welcome"),
    path("main/", views.main, name="main"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile_view, name="profile_view"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path('browse/', views.browse_profiles, name='browse'),
    path('', views.mainpage, name='main'),
    path('browse/', views.browse_profiles, name='browse'),
]