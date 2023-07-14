from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from student import request_views as student_views
from teacher import request_views as teacher_views
from institute import request_views as institute_views
urlpatterns = [
    #students
    path('5.1.1 and 5.1.2/', student_views.table5p1p1and5p1p2),
    path('1.3.4 and 1.3.4.1/', student_views.table1p3p4and1p3p4p1),
    path('5.2.2/', student_views.table5p2p2),
    path('5.3.1/', student_views.table5p3p1),
    path('5.2.1/', student_views.table5p2p1),
    path('5.2.3/', student_views.table5p2p3),
    path('2.7.1/', student_views.table2p7p1),
    #teachers
    path('2.4.1 and 2.4.3/', teacher_views.table2p4p1and2p4p3),
    path('3.1.2 and 3.1.2.1/', teacher_views.table3p1p2and3p1p2p1),
    path('3.1.3/', teacher_views.table3p1p3),
    path('3.4.3/', teacher_views.table3p4p3),
    path('3.4.4/', teacher_views.table3p4p4),
    path('3.5.1/', teacher_views.table3p5p1),
    path('3.5.2/', teacher_views.table3p5p2),
    path('6.3.2/', teacher_views.table6p3p2),
    path('6.3.4/', teacher_views.table6p3p4),
    #institute
    path('1.1.2 and 1.2.2/', institute_views.table1p1p2and1p2p2),
    path('1.1.3 and 1.2.1/', institute_views.table1p1p3and1p2p1),
    path('1.3.2 and 1.3.3/', institute_views.table1p3p2and1p3p3),
    path('2.1.1/', institute_views.table2p1p1),
    path('2.1.2/', institute_views.table2p1p2),
    path('2.4.2 and 3.2.3 and 3.4.2/', institute_views.table2p4p2and3p2p3and3p4p2),
    path('2.5.1/', institute_views.table2p5p1),
    path('2.6.3/', institute_views.table2p6p3),
    path('3.2.1 and 3.2.2 and 3.2.4/', institute_views.table3p2p1and3p2p2and3p2p4),
    path('3.3.2/', institute_views.table3p3p2),
    path('3.6.2/', institute_views.table3p6p2and3p6p2p1),
    path('3.6.3 and 3.6.4/', institute_views.table3p6p3and3p6p4),
    path('3.7.1/', institute_views.table3p7p1),
    path('3.7.2/', institute_views.table3p7p2),
    path('4.1.3/', institute_views.table4p1p3),
    path('4.1.4 and 4.4.1/', institute_views.table4p1p4and4p4p1),
    path('4.2.2 and 4.2.3/', institute_views.table4p2p2and4p2p3),
    path('4.3.4/', institute_views.table4p3p4),
    path('5.1.3/', institute_views.table5p1p3),
    path('5.1.4/', institute_views.table5p1p4),
    path('5.3.3/', institute_views.table5p3p3),
    path('6.2.3/', institute_views.table6p2p3),
    path('6.3.3/', institute_views.table6p3p3),
    path('6.4.2/', institute_views.table6p4p2),
    path('6.5.3/', institute_views.table6p5p3),
]