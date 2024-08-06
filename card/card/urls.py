from django.contrib import admin
from django.urls import path, re_path
from first import views

urlpatterns = [
    path('', views.card, name = 'Визитка 1'),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),
    path("work", views.work, kwargs={"name":"БРЦБ", "time":"2 месяца"}),
    re_path("HR/Eror/Data", views.Type),
    re_path("HR/Eror", views.Eror),
    re_path("HR", views.HR),
]

