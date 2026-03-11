from django.urls import path
from . import views

urlpatterns = [

    path('', views.welcome, name='home'),

    path("register/", views.user_register, name="register"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("main/", views.main, name="main"),
    path("welcome/", views.welcome, name="welcome"),

    path("profile/", views.profile_view, name="profile_view"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),

    path("browse/", views.browse_profiles, name="browse"),

    path("view/<int:id>/", views.view_profile, name="view_profile"),
    path("like/<int:id>/", views.like_profile, name="like_profile"),
    path("message/<int:id>/", views.send_message, name="send_message"),

]