from django.urls import path
from . import views

urlpatterns = [
    path("rich_list/", views.rich_list, name="rich_list"),
]
