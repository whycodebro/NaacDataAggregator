from django.shortcuts import render
from teacher import db_connect_views
# Create your views here.
def table2p4p1and2p4p3(request):
    # Authenticaion of request
    return db_connect_views.table2p4p1and2p4p3(request)

def table3p1p2and3p1p2p1(request):
    # Authenticaion of request
    return db_connect_views.table3p1p2and3p1p2p1(request)

def table3p1p3(request):
    # Authenticaion of request
    return db_connect_views.table3p1p3(request)

def table3p4p3(request):
    # Authenticaion of request
    return db_connect_views.table3p4p3(request)

def table3p4p4(request):
    # Authenticaion of request
    return db_connect_views.table3p4p4(request)

def table3p5p1(request):
    # Authenticaion of request
    return db_connect_views.table3p5p1(request)

def table3p5p2(request):
    # Authenticaion of request
    return db_connect_views.table3p5p2(request)

def table6p3p2(request):
    # Authenticaion of request
    return db_connect_views.table6p3p2(request)

def table6p3p4(request):
    # Authenticaion of request
    return db_connect_views.table6p3p4(request)

def displayhome(request):
    # Authentication of request
    return db_connect_views.displayhome(request)

def display_criteria_page(request):
    #Authentication of request
    return db_connect_views.display_criteria_page(request)

def Teacher_display(request):
    #Authentication of request
    return db_connect_views.Teacher_display(request)

def Award_fellowship_display(request):
    #Authentication of request
    return db_connect_views.Award_fellowship_display(request)


def Revenue_consultancy_corporate_training_display(request):
    #Authentication of request
    return db_connect_views.Revenue_consultancy_corporate_training_display(request)


def Funds_provided_to_teacher_display(request):
    #Authentication of request
    return db_connect_views.Funds_provided_to_teacher_display(request)


def Book_research_published_display(request):
    #Authentication of request
    return db_connect_views.Book_research_published_display(request)

def E_content_devp_display(request):
    #Authentication of request
    return db_connect_views.E_content_devp_display(request)

def Faculty_dev_program_display(request):
    #Authentication of request
    return db_connect_views.Faculty_dev_program_display(request)


def Teacher_collaborative_activity_participation_display(request):
    #Authentication of request
    return db_connect_views.Teacher_collaborative_activity_participation_display(request)

def teacher_tables(request):
    return db_connect_views.teacher_tables(request)

def Teacher_delete(request,id):
    return db_connect_views.Teacher_delete(request,id)

def Award_fellowship_delete(request,id):
    return db_connect_views.Award_fellowship_delete(request,id)

def Revenue_consultancy_corporate_training_delete(request,id):
    return db_connect_views.Revenue_consultancy_corporate_training_delete(request,id)

def Funds_provided_to_teacher_delete(request,id):
    return db_connect_views.Funds_provided_to_teacher_delete(request,id)

def Book_research_published_delete(request,id):
    return db_connect_views.Book_research_published_delete(request,id)

def E_content_devp_delete(request,id):
    return db_connect_views.E_content_devp_delete(request,id)


def Faculty_dev_program_delete(request,id):
    return db_connect_views.Faculty_dev_program_delete(request,id)

def Teacher_collaborative_activity_participation_delete(request,id):
    return db_connect_views.Teacher_collaborative_activity_participation_delete(request,id)

def Teacher_add(request):
    return db_connect_views.Teacher_add(request)

def Award_fellowship_add(request):
    return db_connect_views.Award_fellowship_add(request)

def Revenue_consultancy_corporate_training_add(request):
    return db_connect_views.Revenue_consultancy_corporate_training_add(request)

def Funds_provided_to_teacher_add(request):
    return db_connect_views.Funds_provided_to_teacher_add(request)

def Book_research_published_add(request):
    return db_connect_views.Book_research_published_add(request)

def E_content_devp_add(request):
    return db_connect_views.E_content_devp_add(request)

def Faculty_dev_program_add(request):
    return db_connect_views.Faculty_dev_program_add(request)

def Teacher_collaborative_activity_participation_add(request):
    return db_connect_views.Teacher_collaborative_activity_participation_add(request)

def Teacher_add_display(request):
    return db_connect_views.Teacher_add_display(request)

def Award_fellowship_add_display(request):
    return db_connect_views.Award_fellowship_add_display(request)

def Revenue_consultancy_corporate_training_add_display(request):
    return db_connect_views.Revenue_consultancy_corporate_training_add_display(request)

def Funds_provided_to_teacher_add_display(request):
    return db_connect_views.Funds_provided_to_teacher_add_display(request)

def Book_research_published_add_display(request):
    return db_connect_views.Book_research_published_add_display(request)

def E_content_devp_add_display(request):
    return db_connect_views.E_content_devp_add_display(request)

def Faculty_dev_program_add_display(request):
    return db_connect_views.Faculty_dev_program_add_display(request)

def Teacher_collaborative_activity_participation_add_display(request):
    return db_connect_views.Teacher_collaborative_activity_participation_add_display(request)

def Teacher_edit_display(request,id):
    return db_connect_views.Teacher_edit_display(request,id)

def Award_fellowship_edit_display(request,id):
    return db_connect_views.Award_fellowship_edit_display(request,id)

def Revenue_consultancy_corporate_training_edit_display(request,id):
    return db_connect_views.Revenue_consultancy_corporate_training_edit_display(request,id)

def Funds_provided_to_teacher_edit_display(request,id):
    return db_connect_views.Funds_provided_to_teacher_edit_display(request,id)

def Book_research_published_edit_display(request,id):
    return db_connect_views.Book_research_published_edit_display(request,id)

def E_content_devp_edit_display(request,id):
    return db_connect_views.E_content_devp_edit_display(request,id)

def Faculty_dev_program_edit_display(request,id):
    return db_connect_views.Faculty_dev_program_edit_display(request,id)

def Teacher_collaborative_activity_participation_edit_display(request,id):
    return db_connect_views.Teacher_collaborative_activity_participation_edit_display(request,id)

def Teacher_edit(request,id):
    return db_connect_views.Teacher_edit(request,id)

def Award_fellowship_edit(request,id):
    return db_connect_views.Award_fellowship_edit(request,id)

def Revenue_consultancy_corporate_training_edit(request,id):
    return db_connect_views.Revenue_consultancy_corporate_training_edit(request,id)

def Funds_provided_to_teacher_edit(request,id):
    return db_connect_views.Funds_provided_to_teacher_edit(request,id)

def Book_research_published_edit(request,id):
    return db_connect_views.Book_research_published_edit(request,id)

def E_content_devp_edit(request,id):
    return db_connect_views.E_content_devp_edit(request,id)

def Faculty_dev_program_edit(request,id):
    return db_connect_views.Faculty_dev_program_edit(request,id)

def Teacher_collaborative_activity_participation_edit(request,id):
    return db_connect_views.Teacher_collaborative_activity_participation_edit(request,id)

def Teacher_bulk_upload(request):
    return db_connect_views.Teacher_bulk_upload(request)
