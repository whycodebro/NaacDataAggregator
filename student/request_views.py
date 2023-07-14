from django.shortcuts import render
from student import db_connect_views
# Create your views here.

def table1p3p4and1p3p4p1(request):
    # Authenticaion of request
    return db_connect_views. table1p3p4and1p3p4p1(request)

def table2p7p1(request):
    # Request Authentication and checks here
    return db_connect_views.table2p7p1(request)

def table5p1p1and5p1p2(request):
    # Authenticaion of request
    return db_connect_views. table5p1p1and5p1p2(request)

def table5p2p1(request):
    # Authenticaion of request
    return db_connect_views.table5p2p1(request)

def table5p2p2(request):
    # Authenticaion of request
    return db_connect_views. table5p2p2(request)

def table5p2p3(request):
    # Authenticaion of request
    return db_connect_views. table5p2p3(request)

def table5p3p1(request):
    # Authenticaion of request
    return db_connect_views. table5p3p1(request)

def displayhomestudent(request):
    # Authentication of request
    return db_connect_views.displayhomestudent(request)

def displayacademicinfo(request):
    #Authentication of request
    return db_connect_views.displayacademicinfo(request)

def Student_display(request):
    return db_connect_views.Student_display(request)


def Scholarship_display(request):
    # Authentication of request
    return db_connect_views.Scholarship_display(request)


def Placement_internship_project_display(request):
    # Authentication of request
    return db_connect_views.Placement_internship_project_display(request)


def Competative_exam_display(request):
    # Authentication of request
    return db_connect_views.Competative_exam_display(request)


def Sports_cultural_award_display(request):
    # Authentication of request
    return db_connect_views.Sports_cultural_award_display(request)


def Student_collaborative_activity_participation_display(request):
    # Authentication of request
    return db_connect_views.Student_collaborative_activity_participation_display(request)

def student_tables(request):
    return db_connect_views.student_tables(request)

def Student_delete(request,id):
    return db_connect_views.Student_delete(request,id)

def Scholarship_delete(request,id):
    return db_connect_views.Scholarship_delete(request,id)

def Placement_internship_project_delete(request,id):
    return db_connect_views.Placement_internship_project_delete(request,id)


def Competative_exam_delete(request,id):
    return db_connect_views.Competative_exam_delete(request,id)


def Sports_cultural_award_delete(request,id):
    return db_connect_views.Sports_cultural_award_delete(request,id)


def Student_collaborative_activity_participation_delete(request,id):
    return db_connect_views.Student_collaborative_activity_participation_delete(request,id)

def Student_add(request):
    return db_connect_views.Student_add(request)

def Scholarship_add(request):
    return db_connect_views.Scholarship_add(request)

def Placement_internship_project_add(request):
    return db_connect_views.Placement_internship_project_add(request)

def Competative_exam_add(request):
    return db_connect_views.Competative_exam_add(request)

def Sports_cultural_award_add(request):
    return db_connect_views.Sports_cultural_award_add(request)

def Student_collaborative_activity_participation_add(request):
    return db_connect_views.Student_collaborative_activity_participation_add(request)

def Student_edit_display(request, id):
    return db_connect_views.Student_edit_display(request,id)

def Scholarship_add_display(request):
    return db_connect_views.Scholarship_add_display(request)

def Placement_internship_project_add_display(request):
    return db_connect_views.Placement_internship_project_add_display(request)

def Competative_exam_add_display(request):
    return db_connect_views.Competative_exam_add_display(request)

def Sports_cultural_award_add_display(request):
    return db_connect_views.Sports_cultural_award_add_display(request)

def Student_collaborative_activity_participation_add_display(request):
    return db_connect_views.Student_collaborative_activity_participation_add_display(request)

def Scholarship_edit_display(request,id):
    return db_connect_views.Scholarship_edit_display(request,id)

def Placement_internship_project_edit_display(request,id):
    return db_connect_views.Placement_internship_project_edit_display(request,id)

def Competative_exam_edit_display(request,id):
    return db_connect_views.Competative_exam_edit_display(request,id)

def Sports_cultural_award_edit_display(request,id):
    return db_connect_views.Sports_cultural_award_edit_display(request,id)

def Student_collaborative_activity_participation_edit_display(request,id):
    return db_connect_views.Student_collaborative_activity_participation_edit_display(request,id)

def Student_edit(request,id):
    return db_connect_views.Student_edit(request,id)

def Scholarship_edit(request,id):
    return db_connect_views.Scholarship_edit(request,id)

def Placement_internship_project_edit(request,id):
    return db_connect_views.Placement_internship_project_edit(request,id)

def Competative_exam_edit(request,id):
    return db_connect_views.Competative_exam_edit(request,id)

def Sports_cultural_award_edit(request,id):
    return db_connect_views.Sports_cultural_award_edit(request,id)

def Student_collaborative_activity_participation_edit(request,id):
    return db_connect_views.Student_collaborative_activity_participation_edit(request,id)

def Student_bulk_upload(request):
    return db_connect_views.Student_bulk_upload(request)


