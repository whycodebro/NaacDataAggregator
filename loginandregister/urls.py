from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from loginandregister import views
urlpatterns = [
    path('login/', views.displayhomepage),
    path('login/validateuser/', views.validateuser),
    path('logout/',views.logout),
]
