from django.urls import path
from . import views

urlpatterns = [
    path("richlist/", views.richlist, name="richlist"),
]
