from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('query_builder/', views.query_builder,name="query_builder"),
    path('query_table/', views.query_table,name="query_table"),
]