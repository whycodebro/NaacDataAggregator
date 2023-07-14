import datetime

from django.shortcuts import render
from institute import response_views
import xlwt
from django.http import HttpResponse,HttpResponseRedirect
from institute.models import *
from institute.forms import *
from student.models import *
from teacher.models import *
from student.db_connect_views import *
from teacher.db_connect_views import *
#-------------

workbook='wb'
worksheet='ws'
#-----------
def getWorkbookAndWorksheet(filename):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="'+filename+'.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('New Sheet')
    return {workbook:wb,worksheet:ws,'response':response}

def table1p1p2and1p2p2(request):
    #Check DB Connectivity
    dict=getWorkbookAndWorksheet('1.1.2 and 1.2.2')
    wb= dict[workbook]
    ws= dict[worksheet]
    response= dict['response']
    ws.write(0,0, 'Programme Code')
    ws.write(0,1, 'Programme name')
    ws.write(0,2, 'Year of Introduction')
    ws.write(0,3, 'Status if implementation of CBCS/ECS')
    ws.write(0,4, 'Year of Implementation of CBCS/ECS')
    ws.write(0,5, 'Year of Revision')
    ws.write(0,6, 'Percent of Content Modified')
    ws.write(0,7, 'Link to Document')
    program_list= Program_revision.objects.all();
    row=1
    for obj in program_list:
        ws.write(row, 0, obj.program.prog_code)
        ws.write(row, 1, obj.program.prog_name)
        ws.write(row, 2, obj.program.year_of_intro)
        ws.write(row, 3, obj.program.cbcs_ecs_status)
        ws.write(row, 4, obj.program.cbcs_ecs_year_implementation)
        ws.write(row, 5, obj.revision_year)
        ws.write(row, 6, obj.percent_of_cont_modified)
        ws.write(row, 7, obj.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table1p1p3and1p2p1(request):
    #check DB Connectivity
    dict = getWorkbookAndWorksheet('1.1.3 and 1.2.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the Course')
    ws.write(0,1, 'Course Code')
    ws.write(0,2, 'Activities/Content with direct bearing on Employability/ Entrepreneurship/ Skill development')
    ws.write(0,3, 'Year of introduction (during the last five years)')
    ws.write(0,4, 'Link to the relevant document')
    emp_courses= Employbility_course.objects.all()
    row=1
    for obj in emp_courses:
        ws.write(row, 0, obj.course.course_name)
        ws.write(row, 1, obj.course.course_code)
        ws.write(row, 2, obj.activity_performed)
        ws.write(row, 3, obj.course.year_of_intro)
        ws.write(row, 4, obj.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table1p3p2and1p3p3(request):   #see later
    #chaeck Databae connectivity
    dict = getWorkbookAndWorksheet('1.3.2 and 1.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    today= datetime.date.today()
    year= int(today.year)
    row=0
    for i in range(5):
        ws.write_merge(row,row,0,6,str(year-i))
        row=row+1
        ws.write(row,0,'Name of the value added courses (with  30 or more contact hours)offered')
        ws.write(row,1, 'Course Code(if any)')
        ws.write(row,2, 'Year of offering')
        ws.write(row,3, 'No. of times offered during the same year')
        ws.write(row,4, 'Duration of Course')
        ws.write(row,5, 'Number of students enrolled in the year')
        ws.write(row,6,'Number of Students completing the course  in the year')
        row=row+1
        value_courses = Value_added_courses.objects.filter(year=year-i)
        for obj in value_courses:
            ws.write(row, 0, obj.course.course_name)
            ws.write(row, 1, obj.course.course_code)
            ws.write(row, 2, obj.year)
            ws.write(row, 3, obj.no_of_times_offered_in_a_year)
            ws.write(row, 4, obj.course.course_duration)
            ws.write(row, 6, obj.number_of_students_completing_course)
            row=row+1
        row=row+2
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p1p1(request):  #see later
    # chaeck Databae connectivity
    dict = getWorkbookAndWorksheet('2.1.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    today = datetime.date.today()
    year = int(today.year)
    row = 0
    data = Category_seat_reservation.objects.raw("SELECT 1 as id,SUM(number_of_seats_sanctioned) as sum_sanctioned,SUM(number_of_students_admitted) as sum_admitted, year,program_id FROM public.institute_category_seat_reservation GROUP BY program_id, year;")

    for i in range(5):
        ws.write_merge(row,row,0,3,str(year-i))
        row=row+1
        ws.write(row,0,'Programme name')
        ws.write(row,1, 'Programme Code')
        ws.write(row,2, 'Number of seats sanctioned')
        ws.write(row,3, 'Number of students admitted')
        row=row+1
        list_data= []
        for obj in data:
            if obj.year == (year-i):
                list_data.append(obj)
        for obj in list_data:
            prog= Program.objects.get(prog_id=obj.program_id)
            ws.write(row, 0, prog.prog_name)
            ws.write(row, 1, prog.prog_code)
            ws.write(row, 2, obj.sum_sanctioned)
            ws.write(row, 3, obj.sum_admitted)
            row=row+1
        row=row+2
    wb.save(response)
    return response_views.excel_file_report(response)


def table2p1p2(request): #see later
    #Check db connection
    dict = getWorkbookAndWorksheet('2.1.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,0,1,6,'Number of  seats earmarked for reserved category as per GOI or State ')
    ws.write_merge(0,0,7,12,'Number of students admitted from the reserved category')
    ws.write(1,1,'SC')
    ws.write(1,2,'ST')
    ws.write(1,3,'OBC')
    ws.write(1,4,'Divyangjan')
    ws.write(1,5,'GEN')
    ws.write(1,6,'Others')
    ws.write(1, 7, 'SC')
    ws.write(1, 8, 'ST')
    ws.write(1, 9, 'OBC')
    ws.write(1, 10, 'Divyangjan')
    ws.write(1, 11, 'GEN')
    ws.write(1, 12, 'Others')
    today = datetime.date.today()
    year = int(today.year)
    row=2
    class Cat:
        pass

    for i in range(5):
        data= Category_seat_reservation.objects.raw("SELECT 1 as id,SUM(number_of_seats_sanctioned) as sum_sanctioned,SUM(number_of_students_admitted) as sum_admitted,category_type FROM public.institute_category_seat_reservation WHERE year="+str(year-i)+" GROUP BY category_type;")
        sc = Cat()
        sc.sum_sanctioned = 0
        sc.sum_admitted = 0
        st = Cat()
        st.sum_sanctioned = 0
        st.sum_admitted = 0
        obc = Cat()
        obc.sum_sanctioned = 0
        obc.sum_admitted = 0
        div = Cat()
        div.sum_sanctioned = 0
        div.sum_admitted = 0
        gen = Cat()
        gen.sum_sanctioned = 0
        gen.sum_admitted = 0
        oth = Cat()
        oth.sum_sanctioned = 0
        oth.sum_admitted = 0
        for obj in data:
            if obj.category_type=='SC':
                sc=obj
            elif obj.category_type=='ST':
                st=obj
            elif obj.category_type=='Divyangjan':
                div=obj
            elif obj.category_type=='OBC':
                obc=obj
            elif obj.category_type=='General':
                gen=obj
            elif obj.category_type=='Others':
                oth=obj
        ws.write(row,0,year-i)
        ws.write(row,1,sc.sum_sanctioned)
        ws.write(row,2,st.sum_sanctioned)
        ws.write(row,3,obc.sum_sanctioned)
        ws.write(row,4,div.sum_sanctioned)
        ws.write(row,5,gen.sum_sanctioned)
        ws.write(row,6,oth.sum_sanctioned)
        ws.write(row, 7, sc.sum_admitted)
        ws.write(row, 8, st.sum_admitted)
        ws.write(row, 9, obc.sum_admitted)
        ws.write(row, 10, div.sum_admitted)
        ws.write(row, 11, gen.sum_admitted)
        ws.write(row, 12, oth.sum_admitted)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p4p2and3p2p3and3p4p2(request): # Not in database
    # Check db connection
    dict = getWorkbookAndWorksheet('2.4.2 and 3.2.3 and 3.4.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the Research scholar')
    ws.write(0,1,'Year of registration of the scholar ')
    ws.write(0,3, 'Guide allotment letter web link to be provided ')
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p5p1(request):  #see later
    # Check db connection
    dict = getWorkbookAndWorksheet('2.5.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    today = datetime.date.today()
    year = int(today.year)
    row = 0
    for i in range(5):
        ws.write_merge(row,row,0,4,str(year-i))
        row=row+1
        ws.write(row,0,'Programme Name')
        ws.write(row,1, 'Programme Code')
        ws.write(row,2, 'Semester/ year')
        ws.write(row,3, 'Last date of the last semester-end/ year- end examination')
        ws.write(row,4, 'Date of declaration of results of semester-end/ year- end examination')
        row=row+1
        data= Exam_result.objects.filter(year= year-i)
        for obj in data:
            ws.write(row,0,obj.program.prog_name)
            ws.write(row,1,obj.program.prog_code)
            ws.write(row,2,obj.semester)
            ws.write(row,3,str(obj.exam_last_date))
            ws.write(row,4,str(obj.result_date))
            row=row+1
        row=row+2
    wb.save(response)
    return response_views.excel_file_report(response)


def table2p6p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('2.6.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Program Code')
    ws.write(0, 1, 'Program Name')
    ws.write(0, 2, 'Number of students appeared in the final year examination')
    ws.write(0, 3, 'Number of students passed in final year examination')
    today = datetime.date.today()
    year = int(today.year)
    program_list= Exam_result.objects.filter(year=year)
    row=1
    for obj in program_list:
        ws.write(row, 0, obj.program.prog_code)
        ws.write(row, 1, obj.program.prog_name)
        ws.write(row, 2, obj.no_of_students_appeared)
        ws.write(row, 3, obj.no_of_students_passed)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p2p1and3p2p2and3p2p4(request): #not in database
    # Check db connection
    dict = getWorkbookAndWorksheet('3.2.1 and 3.2.2 and 3.2.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Sl.no.')
    ws.write(0, 1, 'Name of the Principal Investigator/ Co Investigator (if applicable)')
    ws.write(0, 2, 'Name of the Funding agency ')
    ws.write(0, 3, 'Type (Government/Non-Government)')
    ws.write(0, 4, 'Department of Principal Investigator/ Co Investigator')
    ws.write(0, 5, 'Year of Award')
    ws.write(0, 6, 'Funds provided (INR in lakhs) ')
    ws.write(0, 7, 'Duration of the project')
    wb.save(response)
    return response_views.excel_file_report(response)


def table3p3p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.3.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Name of the workshop/ seminar')
    ws.write(0,2, 'Number of Participants')
    ws.write(0,3, 'Date From – To')
    ws.write(0,4, 'Link to the Activity report on the website')
    row=1
    today = datetime.date.today()
    year = int(today.year)
    workshop_list= Workshop_seminar.objects.filter(year_of_conduction__gte=year-5)
    for obj in workshop_list:
        ws.write(row, 0, obj.year_of_conduction)
        ws.write(row, 1, obj.name_of_workshop_seminar)
        ws.write(row, 2, obj.no_of_participants)
        ws.write(row, 3, str(obj.start_date)+' to '+str(obj.end_date))
        ws.write(row, 4, obj.activity_report_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)


def table3p6p2and3p6p2p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.6.2 and 3.6.2.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the activity')
    ws.write(0,1, 'Name of the Award/recognition')
    ws.write(0,2, 'Name of the Awarding government/ government recognised bodies')
    ws.write(0,3, 'Year of Award')
    today = datetime.date.today()
    year = int(today.year)
    activity_list= Extension_activity_award.objects.filter(year_of_awarding__gt=year-5)
    row=1
    for obj in activity_list:
        ws.write(row, 0, obj.activity_name)
        ws.write(row, 1, obj.award_name)
        ws.write(row, 2, obj.awarding_agency_name)
        ws.write(row, 3, obj.year_of_awarding)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p6p3and3p6p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.6.3 and 3.6.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the activity')
    ws.write(0,1, 'Organising unit/ agency/ collaborating agency')
    ws.write(0,2, 'Name of the scheme')
    ws.write(0,3, 'Year of the activity ')
    ws.write(0,4, 'Number of students participated in such activities')
    prog_list= Prof_dev_skill_enhan_ext_outrch_prog.objects.raw("SELECT * FROM public.institute_prof_dev_skill_enhan_ext_outrch_prog WHERE type='outreach';")
    row=1
    for obj in prog_list:
        ws.write(row, 0, obj.program_title)
        ws.write(row, 1, obj.agency_or_organizing_unit)
        ws.write(row, 2, obj.outrch_prog_scheme_name)
        ws.write(row, 3, str(obj.start_date)+' to '+str(obj.end_date))
        ws.write(row, 4, obj.no_of_participants)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p7p1(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('3.7.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Sl. No.')
    ws.write(0,1, 'Title of the collaborative activity')
    ws.write(0,2, 'Name of the collaborating agency with contact details')
    ws.write(0,3, 'Name of the participant ')
    ws.write(0,4, 'Year of collaboration')
    ws.write(0,5, 'Duration')
    ws.write(0,6,'Nature of the activity')
    ws.write(0,7,'Link to the relavant document')
    today = datetime.date.today()
    year = int(today.year)
    student_list= Student_collaborative_activity_participation.objects.all()
    row=1
    for obj in student_list:
        ws.write(row, 0, row)
        ws.write(row, 1, obj.activity.title_of_activity)
        ws.write(row, 2, obj.activity.collaborating_agency_name)
        ws.write(row, 3, obj.student.student.user.first_name+' '+obj.student.student.user.last_name)
        ws.write(row, 4, obj.activity.year_of_collaboration)
        ws.write(row, 5, obj.activity.duration)
        ws.write(row, 6, obj.activity.nature_of_activity)
        ws.write(row, 7, obj.activity.document_link)
        row=row+1

    teacher_list= Teacher_collaborative_activity_participation.objects.all()
    for obj in teacher_list:
        ws.write(row, 0, row)
        ws.write(row, 1, obj.activity.title_of_activity)
        ws.write(row, 2, obj.activity.collaborating_agency_name)
        ws.write(row, 3, obj.teacher.teacher.user.first_name+' '+obj.teacher.teacher.user.last_name)
        ws.write(row, 4, obj.activity.year_of_collaboration)
        ws.write(row, 5, obj.activity.duration)
        ws.write(row, 6, obj.activity.nature_of_activity)
        ws.write(row, 7, obj.activity.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p7p2(request):        #see later
    # Check db connection
    dict = getWorkbookAndWorksheet('3.7.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Organisation with which MoU is signed')
    ws.write(0,1, 'Name of the institution/ industry/ corporate house')
    ws.write(0,2, 'Year of signing MoU')
    ws.write(0,3, 'Duration')
    ws.write(0,4, 'List the  actual  activities under each MOU year-wise')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p1p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('4.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Room number or Name  of classrooms/Seminar Hall with LCD / wifi/LAN facilities with room numbers')
    ws.write(0,1, 'Type of ICT facility')
    ws.write(0,2, 'Link to geo tagged photos and master time table')
    ict_list= Ict_facility.objects.all()
    row=1
    for obj in ict_list:
        ws.write(row, 0, obj.room_number)
        ws.write(row, 1, obj.facility_type)
        ws.write(row, 2, obj.link_to_geo_tagged_photos)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p1p4and4p4p1(request):  #table not in database
    # Check db connection
    dict = getWorkbookAndWorksheet('4.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Budget allocated for infrastructure augmentation')
    ws.write(0, 2, 'Expenditure for infrastructure augmentation')
    ws.write(0, 3, 'Total expenditure excluding Salary')
    ws.write(0, 4, 'Expenditure on maintenace of academic facilities (excluding salary for human resources) ')
    ws.write(0, 5, 'Expenditure on maintenance of physical facilities (excluding salary for human resources) ')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p2p2and4p2p3(request):  #see later
    # Check db connection
    dict = getWorkbookAndWorksheet('4.2.2 and 4.2.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    row=0
    today = datetime.date.today()
    year = int(today.year)
    for i in range(5):
        ws.write_merge(row,row,0,4, str(year-i))
        data=E_library_resource.objects.filter(year=year-i)
        row=row+1
        ws.write(row,0, 'Library resources')
        ws.write(row,1, 'If yes, details of memberships/subscriptions ')
        ws.write(row,2, 'Expenditure on subscription to e-journals,  e-books (INR in lakhs)')
        ws.write(row,3, 'Total Library Expenditure')
        ws.write(row,4, 'Link to the relevant document')
        row=row+1
        for obj in data:
            ws.write(row,0,obj.type)
            ws.write(row,1,obj.subscription_details)
            ws.write(row,2,obj.subscription_expenditure)
            ws.write(row,3,obj.total_library_expenditure)
            ws.write(row,4,obj.doc_link)
            row=row+1
        row=row+2
    wb.save(response)
    return response_views.excel_file_report(response)


def table5p1p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.1.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Name of the capability enhancement program')
    ws.write(0,1, 'Date of implementation (DD-MM-YYYY)')
    ws.write(0,2, 'Number of students enrolled')
    ws.write(0,3, 'Name of the agencies/consultants involved with contact details (if any)')
    prog_list= Prof_dev_skill_enhan_ext_outrch_prog.objects.raw("SELECT * FROM public.institute_prof_dev_skill_enhan_ext_outrch_prog WHERE type='capability enhancement';")
    row=1
    for obj in prog_list:
        ws.write(row, 0, obj.program_title)
        ws.write(row, 1, obj.start_date)
        ws.write(row, 2, obj.no_of_participants)
        ws.write(row, 3, obj.agency_or_organizing_unit)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p1p4(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.1.4')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,0,1,2,'Name of the Activity conducted by the HEI  to offer guidance for  competitive examinations offered by the institution during the last five years ')
    ws.write(1,1, 'Name of the Activity conducted by the HEI  to offer guidance for  competitive examinations/ career counselling offered by the institution during the last five years ')
    ws.write(1,2, 'Number of students attended / participated')
    ws.write_merge(0, 1, 3, 3, 'Number of students placed  through campus placement')
    ws.write_merge(0, 1, 4, 4, 'Link to the relevant document')
    hei_list = Hei_guidence_activity.objects.all()
    row=2
    for obj in hei_list:
        ws.write(row, 0, obj.year_of_conduction)
        ws.write(row, 1, obj.activity_name)
        ws.write(row, 2, obj.number_of_students_enrolled)
        ws.write(row, 3, obj.number_of_students_placed)
        ws.write(row, 4, obj.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)


def table5p3p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('5.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Date of event/competition (DD-MM-YYYY)')
    ws.write(0,2, 'Name  of the event/competition')
    sports_list= Sports_cultural_event_by_intitution.objects.all()
    row=1
    for obj in sports_list:
        ws.write(row, 0, obj.event_date)
        ws.write(row, 1, obj.event_date)
        ws.write(row, 2, obj.event_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p2p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.2.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Areas of e governance')
    ws.write(0, 1, 'Year of implementation')
    ws.write(0, 2, 'Link to relevant website/ document')
    obj_list= E_governance.objects.all()
    row=1
    for obj in obj_list:
        ws.write(row, 0, obj.type)
        ws.write(row, 1, obj.implementation_year)
        ws.write(row, 2, obj.doc_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p3(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.3.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Dates (from-to) (DD-MM-YYYY)')
    ws.write(0, 1, 'Title of the professional development/ administrative training programs organised for teaching staff(Professional development / administrative training programs)')
    ws.write(0, 2, 'No. of participants')
    obj_list= Prof_dev_skill_enhan_ext_outrch_prog.objects.raw("SELECT * FROM public.institute_prof_dev_skill_enhan_ext_outrch_prog WHERE type='professional development'")
    row= 1
    for obj in obj_list:
        ws.write(row, 0, str(obj.start_date)+' to '+str(obj.end_date))
        ws.write(row, 1, obj.program_title)
        ws.write(row, 2, obj.no_of_participants)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p4p2(request):
    # Check db connection
    dict = getWorkbookAndWorksheet('6.4.2')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Name of the non government funding agencies/ individuals')
    ws.write(0, 2, 'Purpose of the Grant')
    ws.write(0, 3, 'Funds/ Grants received (INR in lakhs)')
    ws.write(0, 4, 'Link to Audited Statement of Accounts reflecting the receipts')
    obj_list= Funds_grants_to_inst.objects.all()
    row=1
    for obj in obj_list:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.ngo_name)
        ws.write(row, 2, obj.grant_purpose)
        ws.write(row, 3, obj.fund_amount)
        ws.write(row, 4, obj.audit_doc_link)
        row= row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p5p3(request): #not in database
    # Check db connection
    dict = getWorkbookAndWorksheet('6.5.3')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Conferences, Seminars, Workshops on quality conducted ')
    ws.write(0, 2, 'Academic Administrative Audit (AAA) and initiation of follow up action')
    ws.write(0, 3, 'Participation in NIRF along with Status. ')
    ws.write(0, 4, 'ISO Certification.  and nature and validity period')
    ws.write(0, 5, 'NBA or any other certification received with program specifications.')
    ws.write(0, 6, 'Collaborative quality initiatives with other institution(s) (Provide name of the institution and activity')
    ws.write(0, 7, 'Orientation programme on quality issues for teachers and students organised by the institution, Date (From-To) (DD-MM-YYYY)')
    wb.save(response)
    return response_views.excel_file_report(response)


def displayhome(request):
    return response_views.htmlpage(request,'institute/home.html', {})

def display_academic_home(request):
    user = request.user
    alluser = Alluser.objects.get(user=user)
    dict_list=[Placement_internship_project_display(request),Competative_exam_display(request),Award_fellowship_display(request),Revenue_consultancy_corporate_training_display(request),Book_research_published_display(request),E_content_devp_display(request),Faculty_dev_program_display(request),Exam_result_display(request),]
    dict={'alluser':alluser, 'dict_list':dict_list,}
    return render(request,'institute/academic_home.html', dict)

def display_account_home(request):
    user= request.user
    alluser= Alluser.objects.get(user=user)
    dict_list=[Scholarship_display(request),Revenue_consultancy_corporate_training_display(request),Funds_provided_to_teacher_display(request),Facility_dev_for_consultancy_display(request),Funds_grants_to_inst_display(request)]
    dict = {'alluser': alluser, 'dict_list': dict_list, }
    return render(request, 'institute/academic_home.html', dict)

def display_sport_home(request):
    user = request.user
    alluser = Alluser.objects.get(user=user)
    dict_list = [Sports_cultural_award_display(request),Sports_cultural_event_by_intitution_display(request)]
    dict = {'alluser': alluser, 'dict_list': dict_list, }
    return render(request, 'institute/academic_home.html', dict)

def display_library_home(request):
    user = request.user
    alluser = Alluser.objects.get(user=user)
    dict_list = [Book_research_published_display(request),E_library_resource_display(request)]
    dict = {'alluser': alluser, 'dict_list': dict_list, }
    return render(request, 'institute/academic_home.html', dict)

def display_naac_cod_home(request):
    user = request.user
    alluser= Alluser.objects.get(user=user)
    dict_list = []
    dict = {'alluser': alluser, 'dict_list': dict_list, 'criteria_button':True}
    return render(request, 'institute/academic_home.html', dict)

def display_admin_home(request):
    user = request.user
    alluser = Alluser.objects.get(user=user)
    dict_list = [Teacher_display(request),Student_display(request)]
    dict = {'alluser': alluser, 'dict_list': dict_list, }
    return render(request, 'institute/academic_home.html', dict)

def display_criteria_page(request):
    #Database and all
    return response_views.htmlpage(request, 'teacher/criteriapage.html',{})

def Program_display(request):
    stu_list = Program.objects.all()
    heading_list = ['prog_name', 'prog_type', 'year_of_intro', 'prog_head_id']  # Imp
    alt_heading_list = ['Program Name', 'Program Type', 'Year of Introduction', 'Program Head']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['prog_head_id'] = stu.prog_head_id  # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.prog_id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Program_form()  # Imp

    temp_dict = {'table_name': 'Programs', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Program_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend

def Collaborative_activity_display(request):
    stu_list = Collaborative_activity.objects.all()
    heading_list = ['title_of_activity', 'year_of_collaboration', 'nature_of_activity']  # Imp
    alt_heading_list = ['Title', 'Collaboration Year', 'Nature of Activity']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Collaborative_activity_form()  # Imp

    temp_dict = {'table_name': 'Collaborative Activities', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Collaborative_activity_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend

def Facility_dev_for_consultancy_display(request):
    stu_list = Facility_dev_for_consultancy.objects.all()
    heading_list = ['facility_developed_name', 'year_of_development', 'consultancy_name']  # Imp
    alt_heading_list = ['Facility Name', 'Development Year', 'Name of Consultancy']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Facilities Developed for Consultancy', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Facility_dev_for_consultancy_edit_display',
                 'deleteurl': 'Facility_dev_for_consultancy_delete', 'addurl':'Facility_dev_for_consultancy_add_display'}
    return temp_dict

def Ict_facility_display(request):
    stu_list = Ict_facility.objects.all()
    heading_list = ['program', 'facility_type']  # Imp
    alt_heading_list = ['Program', 'Type of Facility']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['program']=stu.program
        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Ict_facility_form()  # Imp

    temp_dict = {'table_name': 'ICT facilities', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Ict_facility_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend

def Course_display(request):
    stu_list = Course.objects.all()
    heading_list = ['program', 'course_code','course_name','year_of_intro']  # Imp
    alt_heading_list = ['Program', 'Course Code', 'Course Name', 'Year of Introduction']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['program'] = stu.program
        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Course_form()  # Imp

    temp_dict = {'table_name': 'Courses', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Course_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Students_enrolled_in_course_display(request):
    stu_list = Students_enrolled_in_course.objects.all()
    heading_list = ['course', 'year', 'number_of_students']  # Imp
    alt_heading_list = ['Course', 'Year', 'number_of_students']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['course'] = stu.course

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Students_enrolled_in_course_form()  # Imp

    temp_dict = {'table_name': 'Students Enrolled In Course', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Students_enrolled_in_course_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Value_added_courses_display(request):
    stu_list = Value_added_courses.objects.all()
    heading_list = ['course', 'year', 'no_of_times_offered_in_a_year', 'number_of_students_completing_course']  # Imp
    alt_heading_list = ['Course', 'Year', 'Number Of Times Offered In A Year',
                        'Number Of Students Completing Course']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['course'] = stu.course

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Value_added_courses_form()  # Imp

    temp_dict = {'table_name': 'Value Added Courses', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Value_added_courses_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Employbility_course_display(request):
    stu_list = Employbility_course.objects.all()
    heading_list = ['course', 'activity_performed']  # Imp
    alt_heading_list = ['Course', 'Activity Performed']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['course'] = stu.course

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Employbility_course_form()  # Imp

    temp_dict = {'table_name': 'Employbility Course', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Employbility_course_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Category_seat_reservation_display(request):
    stu_list = Category_seat_reservation.objects.all()
    heading_list = ['program', 'year', 'category_type', 'number_of_seats_sanctioned',
                    'number_of_students_admitted']  # Imp
    alt_heading_list = ['Program', 'Year', 'Category Type', 'Number Of Seats Sanctioned',
                        'Number Of Students Admitted']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['program'] = stu.program

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Category_seat_reservation_form()  # Imp

    temp_dict = {'table_name': 'Category Seat Reservation', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Category_seat_reservation_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Exam_result_display(request):
    stu_list = Exam_result.objects.all()
    heading_list = ['program', 'year', 'semester', 'exam_last_date', 'result_date', 'no_of_students_appeared',
                    'no_of_students_passed']  # Imp
    alt_heading_list = ['Program', 'Year', 'Semester', 'Exam Last Date', 'Result Date', 'Number Of Students Appeared',
                        'Number Of Students Passed']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['program'] = stu.program

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Exam Result', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Exam_result_edit_display',
                 'deleteurl': 'Exam_result_delete','addurl':'Exam_result_add_display'}
    return temp_dict


def Program_revision_display(request):
    stu_list = Program_revision.objects.all()
    heading_list = ['program', 'revision_year', 'percent_of_cont_modified']  # Imp
    alt_heading_list = ['Program', 'Revision Year', 'percent_of_cont_modified']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['program'] = stu.program

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Program_revision_form()  # Imp

    temp_dict = {'table_name': 'Program Revision', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Program_revision_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Mou_display(request):
    stu_list = Mou.objects.all()
    heading_list = ['other_party_name', 'institute_name', 'year_of_signing', 'duration']  # Imp
    alt_heading_list = ['Other Party Name', 'Institute Name', 'Year Of Signing', 'Duration']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Mou_form()  # Imp

    temp_dict = {'table_name': 'MOU', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Mou_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Mou_activity_display(request):
    stu_list = Mou_activity.objects.all()
    heading_list = ['mou', 'year', 'activity_title']  # Imp
    alt_heading_list = ['MOU', 'Year', 'Activity Title']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['mou'] = stu.mou

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Mou_activity_form()  # Imp

    temp_dict = {'table_name': 'MOU Activity', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Mou_activity_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Workshop_seminar_display(request):
    stu_list = Workshop_seminar.objects.all()
    heading_list = ['name_of_workshop_seminar', 'year_of_conduction', 'no_of_participants', 'start_date',
                    'end_date']  # Imp
    alt_heading_list = ['Name Of Workshop Seminar', 'Year Of Conduction', 'Number Of Participants', 'Start Date',
                        'End Date']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Workshop_seminar_form()  # Imp

    temp_dict = {'table_name': 'Workshop Seminar', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Workshop_seminar_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Hei_guidence_activity_display(request):
    stu_list = Hei_guidence_activity.objects.all()
    heading_list = ['activity_name', 'year_of_conduction', 'number_of_students_enrolled',
                    'number_of_students_placed']  # Imp
    alt_heading_list = ['Activity Name', 'Year Of Conduction', 'Number Of Students Enrolled',
                        'Number Of Students Placed']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Hei_guidence_activity_form()  # Imp

    temp_dict = {'table_name': 'HEI Guidence Activity', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Hei_guidence_activity_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Sports_cultural_event_by_intitution_display(request):
    stu_list = Sports_cultural_event_by_intitution.objects.all()
    heading_list = ['event_name', 'event_date']  # Imp
    alt_heading_list = ['Event Name ', 'Event Date']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Sports Cultural Event By Intitution', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Sports_cultural_event_by_intitution_edit_display',
                 'deleteurl': 'Sports_cultural_event_by_intitution_delete','addurl':'Sports_cultural_event_by_intitution_add_display'}
    return temp_dict


def E_governance_display(request):
    stu_list = E_governance.objects.all()
    heading_list = ['type', 'implementation_year', ]  # Imp
    alt_heading_list = ['Type ', 'Implementation Year']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = E_governance_form()  # Imp

    temp_dict = {'table_name': 'E-Governance', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'E_governance_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Extension_activity_award_display(request):
    stu_list = Extension_activity_award.objects.all()
    heading_list = ['activity_name', 'award_name', 'awarding_agency_name', 'year_of_awarding']  # Imp
    alt_heading_list = ['Activity Name ', 'Award Name', 'Awarding Agency Name', 'Year Of Awarding']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Extension_activity_award_form()  # Imp

    temp_dict = {'table_name': 'Extension Activity Award', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Extension_activity_award_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def Funds_grants_to_inst_display(request):
    stu_list = Funds_grants_to_inst.objects.all()
    heading_list = ['ngo_name', 'grant_purpose', 'year', 'fund_amount']  # Imp
    alt_heading_list = [' NGO Name', 'Grant Purpose', 'Year', 'Fund Amount']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Funds Grants To Institution', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Funds_grants_to_inst_edit_display',
                 'deleteurl': 'Funds_grants_to_inst_delete', 'addurl': 'Funds_grants_to_inst_add_display'}
    return temp_dict


def E_library_resource_display(request):
    stu_list = E_library_resource.objects.all()
    heading_list = ['type', 'subscription_details', 'year', 'subscription_expenditure']  # Imp
    alt_heading_list = ['Type', 'Subscription Details', 'Year', 'Subscription Expenditure']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'E-Library Resource', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'E_library_resource_edit_display',
                 'deleteurl': 'E_library_resource_delete', 'addurl':'E_library_resource_add_display'}
    return temp_dict


def Prof_dev_skill_enhan_ext_outrch_prog_display(request):
    stu_list = Prof_dev_skill_enhan_ext_outrch_prog.objects.all()
    heading_list = ['program_title', 'start_date', 'end_date', 'no_of_participants', 'type',
                    'agency_or_organizing_unit', 'outrch_prog_scheme_name']  # Imp
    alt_heading_list = ['Program Title', 'Start Date', 'End Date', 'Number Of Participants', 'Type',
                        ' Agency Or Organizing Unit', 'Outrch Prog Scheme Name']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Prof_dev_skill_enhan_ext_outrch_prog_form()  # Imp

    temp_dict = {'table_name': 'Prof Dev Skill Enhan Ext Outrch Prog', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'edit_entry',
                 'deleteurl': 'Prof_dev_skill_enhan_ext_outrch_prog_delete', 'form': fm}
    rend = render(request, 'institute/crud.html', temp_dict)
    return rend


def admin_tables(request):
    table_dict={
        'Students': '/student/Student',
        'Teachers': '/teacher/Teacher',
        'Programs': '/institute/Program',
        'Collaborative Activities': '/institute/Collaborative_activity',
        'Facilities Developed for Consultancy':'/institute/Facility_dev_for_consultancy',
        'Ict Facilities':'/institute/Ict_facility',
        'Courses':'/institute/Course',
        'Students Enrolled in Courses': '/institute/Students_enrolled_in_course',
        'Value Added Courses': '/institute/Value_added_courses',
        'Employbility Courses': '/institute/Employbility_course',
        'Category Seat Reservations': '/institute/Category_seat_reservation',
        'Exam Results':'/institute/Exam_result',
        'Program Revision': '/institute/Program_revision',
        'MOUs': '/institute/Mou',
        'MOU Activities': '/institute/Mou_activity',
        'Workshop Seminars': '/institute/Workshop_seminar',
        'HEI Guidence Activities':'/institute/Hei_guidence_activity',
        'Sports and Cultural Event by Institution':'/institute/Sports_cultural_event_by_intitution',
        'E-Governance':'/institute/E_governance',
        'Extension Activity Awards':'/institute/Extension_activity_award',
        'Funds Grant to Institution':'/institute/Funds_grants_to_inst',
        'E-library Resources':'/institute/E_library_resource',
        'Professional Development/ Skill Enhancement/ Outreach Program': '/institute/Prof_dev_skill_enhan_ext_outrch_prog'
    }
    rend = render(request, 'institute/tables.html', {'table_dict':table_dict})
    return rend

def Program_delete(request,id):
    obj= Program.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Program')

def Collaborative_activity_delete(request,id):
    obj= Collaborative_activity.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Collaborative_activity')

def Facility_dev_for_consultancy_delete(request,id):
    obj= Facility_dev_for_consultancy.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/account_home')

def Ict_facility_delete(request,id):
    obj= Ict_facility.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Ict_facility')

def Course_delete(request,id):
    obj= Course.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Course')

def Students_enrolled_in_course_delete(request,id):
    obj= Students_enrolled_in_course.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Students_enrolled_in_course')

def Value_added_courses_delete(request,id):
    obj= Value_added_courses.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Value_added_courses')

def Employbility_course_delete(request,id):
    obj= Employbility_course.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Employbility_course')

def Category_seat_reservation_delete(request,id):
    obj= Category_seat_reservation.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Category_seat_reservation')

def Exam_result_delete(request,id):
    obj= Exam_result.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/academic_home')

def Program_revision_delete(request,id):
    obj= Program_revision.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Program_revision')

def Mou_delete(request,id):
    obj= Mou.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Mou')

def Mou_activity_delete(request,id):
    obj= Mou_activity.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Mou_activity')

def Workshop_seminar_delete(request,id):
    obj= Workshop_seminar.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Workshop_seminar')

def Hei_guidence_activity_delete(request,id):
    obj= Hei_guidence_activity.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Hei_guidence_activity')

def Sports_cultural_event_by_intitution_delete(request,id):
    obj= Sports_cultural_event_by_intitution.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/sport_home')

def E_governance_delete(request,id):
    obj= E_governance.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/E_governance')

def Extension_activity_award_delete(request,id):
    obj= Extension_activity_award.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Extension_activity_award')

def Funds_grants_to_inst_delete(request,id):
    obj= Funds_grants_to_inst.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/account_home')

def E_library_resource_delete(request,id):
    obj= E_library_resource.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/library_home')

def Prof_dev_skill_enhan_ext_outrch_prog_delete(request,id):
    obj= Prof_dev_skill_enhan_ext_outrch_prog.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/institute/Prof_dev_skill_enhan_ext_outrch_prog')

def Exam_result_edit_display(request,id):
    obj = Exam_result.objects.get(pk=id)
    fm = Exam_result_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Exam_result_edit', 'heading': 'Exam Results', 'id': id})

def Exam_result_edit(request,id):
    obj = Exam_result.objects.get(pk=id)
    fm = Exam_result_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/academic_home')

def Exam_result_add_display(request):
    fm = Exam_result_form()
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'Exam_result_add', 'heading': 'Exam Results'})
    return rend

def Exam_result_add(request):
    fm=Exam_result_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/academic_home')


def Facility_dev_for_consultancy_edit_display(request,id):
    obj = Facility_dev_for_consultancy.objects.get(pk=id)
    fm = Facility_dev_for_consultancy_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Facility_dev_for_consultancy_edit', 'heading': 'Facility_dev_for_consultancy', 'id': id})

def Facility_dev_for_consultancy_edit(request,id):
    obj = Facility_dev_for_consultancy.objects.get(pk=id)
    fm = Facility_dev_for_consultancy_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/account_home')

def Facility_dev_for_consultancy_add_display(request):
    fm = Facility_dev_for_consultancy_form()
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'Facility_dev_for_consultancy_add', 'heading': 'Facility_dev_for_consultancy'})
    return rend

def Facility_dev_for_consultancy_add(request):
    fm=Facility_dev_for_consultancy_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/account_home')

def Funds_grants_to_inst_edit_display(request,id):
    obj = Funds_grants_to_inst.objects.get(pk=id)
    fm = Funds_grants_to_inst_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Funds_grants_to_inst_edit', 'heading': 'Funds_grants_to_inst', 'id': id})

def Funds_grants_to_inst_edit(request,id):
    obj = Funds_grants_to_inst.objects.get(pk=id)
    fm = Funds_grants_to_inst_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/account_home')

def Funds_grants_to_inst_add_display(request):
    fm = Funds_grants_to_inst_form()
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'Funds_grants_to_inst_add', 'heading': 'Funds_grants_to_inst'})
    return rend

def Funds_grants_to_inst_add(request):
    fm=Funds_grants_to_inst_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/account_home')


def Sports_cultural_event_by_intitution_edit_display(request,id):
    obj = Sports_cultural_event_by_intitution.objects.get(pk=id)
    fm = Sports_cultural_event_by_intitution_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Sports_cultural_event_by_intitution_edit', 'heading': 'Sports_cultural_event_by_intitution', 'id': id})

def Sports_cultural_event_by_intitution_edit(request,id):
    obj = Sports_cultural_event_by_intitution.objects.get(pk=id)
    fm = Sports_cultural_event_by_intitution_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/sport_home')

def Sports_cultural_event_by_intitution_add_display(request):
    fm = Sports_cultural_event_by_intitution_form()
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'Sports_cultural_event_by_intitution_add', 'heading': 'Sports_cultural_event_by_intitution'})
    return rend

def Sports_cultural_event_by_intitution_add(request):
    fm=Sports_cultural_event_by_intitution_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/sport_home')


def E_library_resource_edit_display(request,id):
    obj = E_library_resource.objects.get(pk=id)
    fm = E_library_resource_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'E_library_resource_edit', 'heading': 'E_library_resource', 'id': id})

def E_library_resource_edit(request,id):
    obj = E_library_resource.objects.get(pk=id)
    fm = E_library_resource_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/library_home')

def E_library_resource_add_display(request):
    fm = E_library_resource_form()
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'E_library_resource_add', 'heading': 'E_library_resource'})
    return rend

def E_library_resource_add(request):
    fm=E_library_resource_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/library_home')