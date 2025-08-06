from django.urls import path
from . import views

urlpatterns = [
    path("gt/", views.senddata),
    path("pst/", views.getdata),
]
