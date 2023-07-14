from student import request_views
from samplereportgen import views
from django.urls import path
urlpatterns = [
    path('', views.displayhomepage),
    path('delete/<id>/', views.delete_entry, name='delete_entry'),
    path('edit/<id>/', views.edit_entry, name='edit_entry'),
    path('downloadreport/', request_views.table5p2p2),
]