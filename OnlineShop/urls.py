from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("detail/<int:id>", detail_page, name="detail_page"),
    path("add/", add_page, name="add_page"),
    path("add_action/", add_page_action, name="add_page_action")
]