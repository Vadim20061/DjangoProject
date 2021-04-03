from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", profile_page, name="profile_page"),
    path("register/", register_page, name="register_page"),
    path("register_action/", register_action, name="register_action"),
    path("login/", login_page, name="login_page"),
    path("login_action/", login_action, name="login_action"),
    path("logout_action/", log_out_action, name="log_out_action"),
]