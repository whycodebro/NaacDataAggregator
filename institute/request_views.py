from django.shortcuts import render
from institute import db_connect_views
# Create your views here.

def table1p1p2and1p2p2(request):
    # Request Authentication and checks here
    return db_connect_views.table1p1p2and1p2p2(request)

def table1p1p3and1p2p1(request):
    # Request Authentication and checks here
    return db_connect_views.table1p1p3and1p2p1(request)

def table1p3p2and1p3p3(request):
    # Request Authentication and checks here
    return db_connect_views.table1p3p2and1p3p3(request)

def table2p1p1(request):
    # Request Authentication and checks here
    return db_connect_views.table2p1p1(request)

def table2p1p2(request):
    # Request Authentication and checks here
    return db_connect_views.table2p1p2(request)

def table2p4p2and3p2p3and3p4p2(request):
    # Request Authentication and checks here
    return db_connect_views.table2p4p2and3p2p3and3p4p2(request)

def table2p5p1(request):
    # Request Authentication and checks here
    return db_connect_views.table2p5p1(request)

def table2p6p3(request):
    # Request Authentication and checks here
    return db_connect_views.table2p6p3(request)

def table3p2p1and3p2p2and3p2p4(request):
    # Request Authentication and checks here
    return db_connect_views.table3p2p1and3p2p2and3p2p4(request)

def table3p3p2(request):
    # Request Authentication and checks here
    return db_connect_views.table3p3p2(request)


def table3p6p2and3p6p2p1(request):
    # Request Authentication and checks here
    return db_connect_views.table3p6p2and3p6p2p1(request)

def table3p6p3and3p6p4(request):
    # Request Authentication and checks here
    return db_connect_views.table3p6p3and3p6p4(request)

def table3p7p1(request):
    # Request Authentication and checks here
    return db_connect_views.table3p7p1(request)

def table3p7p2(request):
    # Request Authentication and checks here
    return db_connect_views.table3p7p2(request)

def table4p1p3(request):
    # Request Authentication and checks here
    return db_connect_views.table4p1p3(request)

def table4p1p4and4p4p1(request):
    # Request Authentication and checks here
    return db_connect_views.table4p1p4and4p4p1(request)

def table4p2p2and4p2p3(request):
    # Request Authentication and checks here
    return db_connect_views.table4p2p2and4p2p3(request)

def table4p3p4(request):
    # Request Authentication and checks here
    return db_connect_views.table4p3p4(request)

def table5p1p3(request):
    # Request Authentication and checks here
    return db_connect_views.table5p1p3(request)

def table5p1p4(request):
    # Request Authentication and checks here
    return db_connect_views.table5p1p4(request)

def table5p3p3(request):
    # Request Authentication and checks here
    return db_connect_views.table5p3p3(request)

def table6p2p3(request):
    # Request Authentication and checks here
    return db_connect_views.table6p2p3(request)

def table6p3p3(request):
    # Request Authentication and checks here
    return db_connect_views.table6p3p3(request)

def table6p4p2(request):
    # Request Authentication and checks here
    return db_connect_views.table6p4p2(request)

def table6p5p3(request):
    # Request Authentication and checks here
    return db_connect_views.table6p5p3(request)

def displayhome(request):
    # Request Authentication and checks here
    return db_connect_views.displayhome(request)

def display_academic_home(request):
    # Request Authentication and checks here
    return db_connect_views.display_academic_home(request)

def display_account_home(request):
    # Request Authentication and checks here
    return db_connect_views.display_account_home(request)

def display_sport_home(request):
    # Request Authentication and checks here
    return db_connect_views.display_sport_home(request)

def display_library_home(request):
    return db_connect_views.display_library_home(request)

def display_naac_cod_home(request):
    return db_connect_views.display_naac_cod_home(request)

def display_admin_home(request):
    return db_connect_views.display_admin_home(request)

def display_criteria_page(request):
    #Database and all
    return db_connect_views.display_criteria_page(request)


def Program_display(request):
    return db_connect_views.Program_display(request)

def Collaborative_activity_display(request):
    return db_connect_views.Collaborative_activity_display(request)

def Facility_dev_for_consultancy_display(request):
    return db_connect_views.Facility_dev_for_consultancy_display(request)

def Ict_facility_display(request):
    return db_connect_views.Ict_facility_display(request)

def Course_display(request):
    return db_connect_views.Course_display(request)

def Students_enrolled_in_course_display(request):
    return db_connect_views.Students_enrolled_in_course_display(request)

def Value_added_courses_display(request):
    return db_connect_views.Value_added_courses_display(request)

def Employbility_course_display(request):
    # Request Authentication and checks here
    return db_connect_views.Employbility_course_display(request)


def Category_seat_reservation_display(request):
    # Request Authentication and checks here
    return db_connect_views.Category_seat_reservation_display(request)

def Exam_result_display(request):
    # Request Authentication and checks here
    return db_connect_views.Exam_result_display(request)

def Program_revision_display(request):
    # Request Authentication and checks here
    return db_connect_views.Program_revision_display(request)

def Mou_display(request):
    # Request Authentication and checks here
    return db_connect_views.Mou_display(request)


def Mou_activity_display(request):
    # Request Authentication and checks here
    return db_connect_views.Mou_activity_display(request)

def Workshop_seminar_display(request):
    # Request Authentication and checks here
    return db_connect_views.Workshop_seminar_display(request)

def Hei_guidence_activity_display(request):
    # Request Authentication and checks here
    return db_connect_views.Hei_guidence_activity_display(request)

def Sports_cultural_event_by_intitution_display(request):
    # Request Authentication and checks here
    return db_connect_views.Sports_cultural_event_by_intitution_display(request)

def E_governance_display(request):
    # Request Authentication and checks here
    return db_connect_views.E_governance_display(request)

def Extension_activity_award_display(request):
    # Request Authentication and checks here
    return db_connect_views.Extension_activity_award_display(request)

def Funds_grants_to_inst_display(request):
    # Request Authentication and checks here
    return db_connect_views.Funds_grants_to_inst_display(request)

def E_library_resource_display(request):
    # Request Authentication and checks here
    return db_connect_views.E_library_resource_display(request)

def Prof_dev_skill_enhan_ext_outrch_prog_display(request):
    # Request Authentication and checks here
    return db_connect_views.Prof_dev_skill_enhan_ext_outrch_prog_display(request)


def admin_tables(request):
    return db_connect_views.admin_tables(request)

def Program_delete(request,id):
    return db_connect_views.Program_delete(request,id)

def Collaborative_activity_delete(request,id):
    return db_connect_views.Collaborative_activity_delete(request,id)

def Facility_dev_for_consultancy_delete(request,id):
    return db_connect_views.Facility_dev_for_consultancy_delete(request,id)

def Ict_facility_delete(request,id):
    return db_connect_views.Ict_facility_delete(request,id)

def Course_delete(request,id):
    return db_connect_views.Course_delete(request,id)

def Students_enrolled_in_course_delete(request,id):
    return db_connect_views.Students_enrolled_in_course_delete(request,id)

def Value_added_courses_delete(request,id):
    return db_connect_views.Value_added_courses_delete(request,id)

def Employbility_course_delete(request,id):
    return db_connect_views.Employbility_course_delete(request,id)

def Category_seat_reservation_delete(request,id):
    return db_connect_views.Category_seat_reservation_delete(request,id)

def Exam_result_delete(request,id):
    return db_connect_views.Exam_result_delete(request,id)

def Program_revision_delete(request,id):
    return db_connect_views.Program_revision_delete(request,id)

def Mou_delete(request,id):
    return db_connect_views.Mou_delete(request,id)

def Mou_activity_delete(request,id):
    return db_connect_views.Mou_activity_delete(request,id)

def Workshop_seminar_delete(request,id):
    return db_connect_views.Workshop_seminar_delete(request,id)

def Hei_guidence_activity_delete(request,id):
    return db_connect_views.Hei_guidence_activity_delete(request,id)

def Sports_cultural_event_by_intitution_delete(request,id):
    return db_connect_views.Sports_cultural_event_by_intitution_delete(request,id)

def E_governance_delete(request,id):
    return db_connect_views.E_governance_delete(request,id)

def Extension_activity_award_delete(request,id):
    return db_connect_views.Extension_activity_award_delete(request,id)

def Funds_grants_to_inst_delete(request,id):
    return db_connect_views.Funds_grants_to_inst_delete(request,id)

def E_library_resource_delete(request,id):
    return db_connect_views.E_library_resource_delete(request,id)

def Prof_dev_skill_enhan_ext_outrch_prog_delete(request,id):
    return db_connect_views.Prof_dev_skill_enhan_ext_outrch_prog_delete(request,id)


def Exam_result_edit_display(request,id):
    return db_connect_views.Exam_result_edit_display(request,id)

def Exam_result_edit(request,id):
    return db_connect_views.Exam_result_edit(request,id)

def Exam_result_add_display(request):
    return db_connect_views.Exam_result_add_display(request)

def Exam_result_add(request):
    return db_connect_views.Exam_result_add(request)


def Facility_dev_for_consultancy_edit_display(request,id):
    return db_connect_views.Facility_dev_for_consultancy_edit_display(request,id)

def Facility_dev_for_consultancy_edit(request,id):
    return db_connect_views.Facility_dev_for_consultancy_edit(request,id)

def Facility_dev_for_consultancy_add_display(request):
    return db_connect_views.Facility_dev_for_consultancy_add_display(request)

def Facility_dev_for_consultancy_add(request):
    return db_connect_views.Facility_dev_for_consultancy_add(request)


def Funds_grants_to_inst_edit_display(request,id):
    return db_connect_views.Funds_grants_to_inst_edit_display(request,id)

def Funds_grants_to_inst_edit(request,id):
    return db_connect_views.Funds_grants_to_inst_edit(request,id)

def Funds_grants_to_inst_add_display(request):
    return db_connect_views.Funds_grants_to_inst_add_display(request)

def Funds_grants_to_inst_add(request):
    return db_connect_views.Funds_grants_to_inst_add(request)

def Sports_cultural_event_by_intitution_edit_display(request,id):
    return db_connect_views.Sports_cultural_event_by_intitution_edit_display(request,id)

def Sports_cultural_event_by_intitution_edit(request,id):
    return db_connect_views.Sports_cultural_event_by_intitution_edit(request,id)

def Sports_cultural_event_by_intitution_add_display(request):
    return db_connect_views.Sports_cultural_event_by_intitution_add_display(request)

def Sports_cultural_event_by_intitution_add(request):
    return db_connect_views.Sports_cultural_event_by_intitution_add(request)

def E_library_resource_edit_display(request,id):
    return db_connect_views.E_library_resource_edit_display(request,id)

def E_library_resource_edit(request,id):
    return db_connect_views.E_library_resource_edit(request,id)

def E_library_resource_add_display(request):
    return db_connect_views.E_library_resource_add_display(request)

def E_library_resource_add(request):
    return db_connect_views.E_library_resource_add(request)

