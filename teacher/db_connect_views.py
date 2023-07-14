from django.shortcuts import render
from teacher import response_views
import xlwt
from django.http import HttpResponse,HttpResponseRedirect
from loginandregister.models import Alluser
from teacher.models import *
from teacher.forms import *
import openpyxl
import datetime
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

def table2p4p1and2p4p3(request):
    #connect to DB
    dict = getWorkbookAndWorksheet('2.4.1 and 2.4.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of the Full-time teacher')
    ws.write(0, 1, ' PAN')
    ws.write(0, 2, ' Designation ')
    ws.write(0, 3, ' Year of  appointment ')
    ws.write(0, 4, 'Nature of appointment (Against Sanctioned post, temporary, permanent)')
    ws.write(0, 5, ' Name of the Department')
    ws.write(0, 6, ' Total years of Experience in the same institution')
    ws.write(0, 7, ' Is the teacher still serving the institution/If not last year of the service of Faculty to the Institution')
    teacher_objs= Teacher.objects.all()
    row=1
    for obj in teacher_objs:
        ws.write(row, 0, obj.teacher.user.first_name+' '+obj.teacher.user.last_name)
        ws.write(row, 1, obj.pan_no)
        ws.write(row, 2, obj.designation)
        ws.write(row, 3, obj.appointment_year)
        ws.write(row, 4, obj.nature_of_appointment)
        ws.write(row, 5, obj.prog.prog_name)
        ws.write(row, 6, obj.experience)
        ws.write(row, 7, obj.present_status)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p1p2and3p1p2p1(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.1.2 and 3.1.2.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher provided with seed money')
    ws.write(0,1, 'The amount of seed money (INR in Lakhs)')
    ws.write(0,2, 'Year of receiving')
    ws.write(0,3, 'Link to the policy documents for Sanction of seed money / grants for research from the institution')
    today = datetime.date.today()
    year = int(today.year)
    listFundsProvided = Funds_provided_to_teacher.objects.raw("SELECT * FROM public.teacher_funds_provided_to_teacher WHERE year>="+str(year-5)+";")
    row = 1
    for obj in listFundsProvided:
        ws.write(row, 0, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 1, obj.amount_spend)
        ws.write(row, 2, obj.year)
        ws.write(row, 3, obj.policy_doc_link)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p1p3(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.1.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher awarded national/ international fellowship/financial support')
    ws.write(0,1, 'Name of the award/fellowship')
    ws.write(0,2, 'Year of Award')
    ws.write(0,3, 'Awarding Agency')
    today = datetime.date.today()
    year = int(today.year)
    listAwards = Award_fellowship.objects.raw("SELECT * FROM public.teacher_award_fellowship WHERE award_year>="+str(year-5)+";")
    row = 1
    for obj in listAwards:
        ws.write(row, 0, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 1, obj.award_fellowship_name)
        ws.write(row, 2, obj.award_year)
        ws.write(row, 3, obj.awarding_agency)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p4p3(request): #teacher
    # connect to DB
    dict = getWorkbookAndWorksheet('3.4.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0, 'Title of paper')
    ws.write_merge(0,1,1,1, 'Name of the author')
    ws.write_merge(0,1,2,2, 'Department of teacher')
    ws.write_merge(0,1,3,3, 'Name of journal')
    ws.write_merge(0,1,4,4, 'Year of publication')
    ws.write_merge(0,1,5,5, 'ISSN number')
    ws.write_merge(0,0,6,8, 'Link to the recognition in UGC enlistment of the Journal')
    ws.write(1,6,'Link to Website')
    ws.write(1,7, 'Link to article')
    ws.write(1,8, 'Is listed in UGC Care')
    today = datetime.date.today()
    year = int(today.year)
    papers_objs= Book_research_published.objects.raw("SELECT * FROM public.teacher_book_research_published WHERE type_of_publish='research paper' AND publication_year>"+str(year-5)+";")
    row=2;
    for obj in papers_objs:
        ws.write(row, 0, obj.publish_title)
        ws.write(row, 1, obj.author_name)
        ws.write(row, 2, obj.teacher.prog.prog_name)
        ws.write(row, 3, obj.publisher_journal_name)
        ws.write(row, 4, obj.publication_year)
        ws.write(row, 5, obj.isbn_issn_number)
        ws.write(row, 6, obj.journal_website_link)
        ws.write(row, 7, obj.doc_link)
        ws.write(row, 8, obj.is_listed_in_ugc_care_scopus)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p4p4(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.4.4')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Sl.No')
    ws.write(0,1,'Name of the teacher')
    ws.write(0,2, 'Title of the book/chapters  published')
    ws.write(0,3,'Title of the paper')
    ws.write(0,4,'Title of the proceedings of the conference')
    ws.write(0,5,'Year of publication')
    ws.write(0,6,'ISBN/ISSN number of the proceeding')
    ws.write(0,7,'Whether at the time of publication Affiliating Institution  Was same Yes/NO')
    ws.write(0,8,'Name of the publisher')
    today = datetime.date.today()
    year = int(today.year)
    row=1
    data= Book_research_published.objects.raw("SELECT * FROM public.teacher_book_research_published WHERE publication_year>"+str(year-5)+"AND type_of_publish!='research paper';")
    for obj in data:
        ws.write(row,0,row)
        ws.write(row,1,obj.teacher.teacher.user.first_name+" "+obj.teacher.teacher.user.last_name)
        ws.write(row,2,obj.publish_title)
        ws.write(row,3,obj.book_chapter_title)
        ws.write(row,5,obj.publication_year)
        ws.write(row,6,obj.isbn_issn_number)
        ws.write(row,8,obj.publisher_journal_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p5p1(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('3.5.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teacher-consultants')
    ws.write(0,1, 'Name of consultancy project/corporate training program')
    ws.write(0,2, 'Consulting/Sponsoring agency with contact details')
    ws.write(0,3, 'Year')
    ws.write(0,4, 'Revenue generated (INR in Lakhs)')
    ws.write(0,5, 'Number of trainees')
    today = datetime.date.today()
    year = int(today.year)
    listRevenueConsultancy = Revenue_consultancy_corporate_training.objects.filter(year__gt=year-5)
    row = 1
    for obj in listRevenueConsultancy:
        ws.write(row, 0, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 1, obj.title)
        ws.write(row, 2, obj.consulting_sponsoring_agency_name + ' ' + obj.contact_details)
        ws.write(row, 3, obj.year)
        ws.write(row, 4, obj.revenue_generated)
        ws.write(row, 5, obj.number_of_trainee)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table3p5p2(request):  #see later
    # connect to DB
    dict = getWorkbookAndWorksheet('3.5.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of the teachers/staff')
    ws.write(0,1, 'Name of the facilities developed and department')
    ws.write(0,2, 'Agency seeking training with contact details')
    ws.write(0,3, 'Year')
    ws.write(0,4, 'Name of consultancy')
    ws.write(0,5, 'Total amount spent (INR in Lakhs)')
    wb.save(response)
    return response_views.excel_file_report(response)

def table4p3p4(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('4.3.4')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of the teacher ')
    ws.write(0, 1, 'Name of the module developed')
    ws.write(0, 2, 'Platform on which module is developed ')
    ws.write(0, 3, 'Date of launching e content ')
    ws.write(0, 4, 'Link to the relevant document and facility available in the institution ')
    ws.write(0, 5, 'List of the e-content development facility available ')
    ws.write(0, 6, 'Provide link to videos of the media centre and recording facility')
    teacher_objs = E_content_devp.objects.all()
    row = 1
    for obj in teacher_objs:
        ws.write(row, 0, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 1, obj.module_name)
        ws.write(row, 2, obj.platform_name)
        ws.write(row, 3, str(obj.date_of_launch))
        ws.write(row, 4, obj.doc_link)
        ws.write(row, 5, obj.type)
        ws.write(row, 6, obj.playlist_link)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p2(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('6.3.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Year')
    ws.write(0, 1, 'Name of teacher')
    ws.write(0, 2, 'Name of conference/ workshop attended for which financial support provided')
    ws.write(0, 3, 'Name of the professional body for which membership fee is provided')
    ws.write(0, 4, 'Amount of support')
    teacher_objs = Funds_provided_to_teacher.objects.all()
    row = 1
    for obj in teacher_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 2, obj.name_of_cons_or_research_or_conf)
        ws.write(row, 3, obj.agency_name)
        ws.write(row, 4, obj.amount_spend)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table6p3p4(request):
    # connect to DB
    dict = getWorkbookAndWorksheet('6.3.4')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0, 0, 'Name of teacher who attended the program')
    ws.write(0, 1, 'Title of the program')
    ws.write(0, 2, 'Duration (from – to) (DD-MM-YYYY)')
    teacher_objs = Faculty_dev_program.objects.all()
    row = 1
    for obj in teacher_objs:
        ws.write(row, 0, obj.teacher.teacher.user.first_name + ' ' + obj.teacher.teacher.user.last_name)
        ws.write(row, 1, obj.program_title)
        ws.write(row, 2, str(obj.start_date) + " To " + str(obj.end_date))
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def displayhome(request):
    # Database connectivity and data fetch
    user = request.user
    alluser = Alluser.objects.get(user=user)
    teacher= Teacher.objects.get(teacher=alluser)
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    dict_list=[Award_fellowship_display(request),Revenue_consultancy_corporate_training_display(request),Funds_provided_to_teacher_display(request),Book_research_published_display(request),E_content_devp_display(request),Faculty_dev_program_display(request),Teacher_collaborative_activity_participation_display(request)]
    dict={'alluser': alluser, 'teacher': teacher, 'dict_list':dict_list}
    return response_views.htmlpage(request, 'teacher/home.html',dict)


def Teacher_display(request):
    stu_list = Teacher.objects.all()
    heading_list = ['teacher','pan_no', 'aadhar_no', 'prog', 'designation', 'appointment_year', 'resignation_year',
                    'nature_of_appointment', 'experience', 'contact_number', 'gender', 'present_status',
                    'qualifications']  # Imp
    alt_heading_list = ['Teacher','PAN Number', 'Aadhar Number', 'Program', 'Designation', 'Appointment Year', 'Resignation Year',
                        'Nature Of Appointment', 'Experience', 'Contact Number', 'Gender', 'Present Status',
                        'Qualifications']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['prog'] = stu.prog
        dict['teacher']= stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.teacher_id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Teacher_form()  # Imp

    temp_dict = {'table_name': 'Teacher', 'Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records',
                 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Teacher_edit_display',
                 'deleteurl': 'Teacher_delete', 'bulkaddurl':'Teacher_bulk_upload'}
    return temp_dict


def Award_fellowship_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Award_fellowship.objects.filter(teacher=teacher)
    heading_list = ['award_fellowship_name', 'award_year', 'awarding_agency']  # Imp
    alt_heading_list = ['Award Fellowship_Name', 'Award Year', 'Awarding Agency']  # Imp
    if alluser.user_type != 'Teacher':
        stu_list = Award_fellowship.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher'] = stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Award Fellowship', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Award_fellowship_edit_display',
                 'deleteurl': 'Award_fellowship_delete', 'addurl':'Award_fellowship_add_display'}
    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict


def Revenue_consultancy_corporate_training_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Revenue_consultancy_corporate_training.objects.filter(teacher=teacher)
    heading_list = ['type', 'title', 'consulting_sponsoring_agency_name', 'contact_details', 'year',
                    'revenue_generated', 'number_of_trainee']  # Imp
    alt_heading_list = ['Type', 'Title', 'Consulting Sponsoring Agency Name', 'Contact Details', 'Year',
                        'Revenue Generated', 'Number Of Trainee']
    if alluser.user_type != 'Teacher':
        stu_list = Revenue_consultancy_corporate_training.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher'] = stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Revenue Consultancy Corporate Training', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Revenue_consultancy_corporate_training_edit_display',
                 'deleteurl': 'Revenue_consultancy_corporate_training_delete', 'addurl':'Revenue_consultancy_corporate_training_add_display'}

    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict


def Funds_provided_to_teacher_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Funds_provided_to_teacher.objects.filter(teacher=teacher)
    heading_list = ['agency_name', 'year', 'name_of_cons_or_research_or_conf', 'amount_spend', 'type']  # Imp
    alt_heading_list = ['Agency Name', 'Year', 'Name Of Cons Or Research Or Conf', 'Amount Spend', 'Type']  # Imp
    if alluser.user_type != 'Teacher':
        stu_list = Funds_provided_to_teacher.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher']=stu.teacher

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Funds Provided To Teacher', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Funds_provided_to_teacher_edit_display',
                 'deleteurl': 'Funds_provided_to_teacher_delete', 'addurl':'Funds_provided_to_teacher_add_display'}
    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''

    return temp_dict


def Book_research_published_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Book_research_published.objects.filter(teacher=teacher)
    heading_list = ['book_chapter_title', 'author_name', 'publication_year', 'publisher_journal_name',
                    'type_of_publish', 'publish_title', 'isbn_issn_number', 'institution_name_during_publication',
                    'listed_in_ugc_status', 'is_listed_in_ugc_care_scopus']  # Imp
    alt_heading_list = ['Book Chapter Title', 'Author Name', 'Publication Year', 'Publisher Journal Name',
                        'Type of Publish', 'Publish Title', 'isbn issn Number', 'Institution Name During Publication',
                        'Listed In ugc Status', 'Is Listed In ugc Care Scopus']  # Imp
    if alluser.user_type!='Teacher':
        stu_list = Book_research_published.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher'] = stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Book Research Published', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Book_research_published_edit_display',
                 'deleteurl': 'Book_research_published_delete', 'addurl':'Book_research_published_add_display'}
    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict


def E_content_devp_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = E_content_devp.objects.filter(teacher=teacher)
    heading_list = ['module_name', 'platform_name', 'date_of_launch', 'type']  # Imp
    alt_heading_list = ['Module Name', 'Platform Name', 'Date Of Launch', 'Type']  # Imp
    if alluser.user_type!='Teacher':
        stu_list = E_content_devp.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher'] = stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'E Content Development', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'E_content_devp_edit_display',
                 'deleteurl': 'E_content_devp_delete','addurl':'E_content_devp_add_display'}
    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict


def Faculty_dev_program_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = None
    if alluser.user_type == 'Teacher':
        teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Faculty_dev_program.objects.filter(teacher=teacher)
    heading_list = ['program_title', 'start_date', 'end_date']  # Imp
    alt_heading_list = ['Program Title', 'Start Date', 'End Date']  # Imp
    if alluser.user_type!='Teacher':
        stu_list = Faculty_dev_program.objects.all()
        heading_list.append('teacher')
        alt_heading_list.append('Teacher')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['teacher'] = stu.teacher
        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Faculty Development Program', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Faculty_dev_program_edit_display',
                 'deleteurl': 'Faculty_dev_program_delete','addurl':'Faculty_dev_program_add_display'}

    if alluser.user_type != 'Teacher':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict


def Teacher_collaborative_activity_participation_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = Teacher.objects.get(teacher=alluser)
    stu_list = Teacher_collaborative_activity_participation.objects.filter(teacher=teacher)
    heading_list = ['activity']  # Imp
    alt_heading_list = ['Activity']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['activity'] = stu.activity

        # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name': 'Teacher Collaborative Activity Participation', 'Heading_add_entry': 'Add New Entry',
                 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Teacher_collaborative_activity_participation_edit_display',
                 'deleteurl': 'Teacher_collaborative_activity_participation_delete', 'addurl':'Teacher_collaborative_activity_participation_add_display'}
    return temp_dict

def teacher_tables(request):
    table_dict={
        'Award fellowships':'/teacher/Award_fellowship',
        'Consultancy/Corporate Training Revenue': '/teacher/Revenue_consultancy_corporate_training',
        'Funds Provided':'/teacher/Funds_provided_to_teacher',
        'Books/Research Papers Published':'/teacher/Book_research_published',
        'E-Content Developed':'/teacher/E_content_devp',
        'Faculty Development Programs':'/teacher/Faculty_dev_program',
        'Collaborative Activity Participation':'/teacher/Teacher_collaborative_activity_participation',
    }
    rend= render(request, 'institute/tables.html', {'table_dict':table_dict})
    return rend

def Teacher_delete(request,id):
    teacher=Teacher.objects.get(pk=id)
    alluser=teacher.teacher
    user= alluser.user
    user.delete()
    return HttpResponseRedirect('/institute/admin_home')

def Award_fellowship_delete(request,id):
    obj=Award_fellowship.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Revenue_consultancy_corporate_training_delete(request,id):
    obj=Revenue_consultancy_corporate_training.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Funds_provided_to_teacher_delete(request,id):
    obj=Funds_provided_to_teacher.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Book_research_published_delete(request,id):
    obj=Book_research_published.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def E_content_devp_delete(request,id):
    obj=E_content_devp.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Faculty_dev_program_delete(request,id):
    obj=Faculty_dev_program.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Teacher_collaborative_activity_participation_delete(request,id):
    obj=Teacher_collaborative_activity_participation.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/teacher/home')

def Teacher_add(request):
    fm=Teacher_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/admin_home')

def Award_fellowship_add(request):
    fm=Award_fellowship_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Revenue_consultancy_corporate_training_add(request):
    fm=Revenue_consultancy_corporate_training_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')


def Funds_provided_to_teacher_add(request):
    fm=Funds_provided_to_teacher_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Book_research_published_add(request):
    fm=Book_research_published_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def E_content_devp_add(request):
    fm=E_content_devp_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Faculty_dev_program_add(request):
    fm=Faculty_dev_program_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Teacher_collaborative_activity_participation_add(request):
    fm=Teacher_collaborative_activity_participation_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Teacher_add_display(request):
    fm= Teacher_form()
    rend = render(request, 'institute/form.html',{'form': fm, 'addurl': 'Teacher_add', 'heading': 'Teachers'})
    return rend

def Award_fellowship_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=Award_fellowship_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Award_fellowship_add', 'heading': 'Award Fellowships'})
    return rend


def Revenue_consultancy_corporate_training_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=Revenue_consultancy_corporate_training_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Revenue_consultancy_corporate_training_add', 'heading': 'Revenue Consultancy Corporate Training'})
    return rend

def Funds_provided_to_teacher_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=Funds_provided_to_teacher_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Funds_provided_to_teacher_add', 'heading': 'Funds Provided to the Teacher'})
    return rend

def Book_research_published_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=Book_research_published_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Book_research_published_add', 'heading': 'Book/Research Published'})
    return rend

def E_content_devp_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=E_content_devp_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'E_content_devp_add', 'heading': 'E-Content Development'})
    return rend

def Faculty_dev_program_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    teacher = Teacher.objects.get(teacher=alluser)
    fm=Faculty_dev_program_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Faculty_dev_program_add', 'heading': 'Faculty Development Program'})
    return rend

def Teacher_collaborative_activity_participation_add_display(request):
    alluser=Alluser.objects.get(user=request.user)
    teacher= Teacher.objects.get(teacher=alluser)
    fm=Teacher_collaborative_activity_participation_form(initial={'teacher':teacher})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Teacher_collaborative_activity_participation_add', 'heading': 'Teacher Collaborative Activity Participation'})
    return rend

def Teacher_edit_display(request,id):
    obj = Teacher.objects.get(pk=id)
    fm = Teacher_form(instance=obj)
    rend = render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Teacher_edit', 'heading': 'Teachers', 'id': id})
    return rend

def Award_fellowship_edit_display(request,id):
    obj= Award_fellowship.objects.get(pk=id)
    fm=Award_fellowship_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Award_fellowship_edit', 'heading': 'Award Fellowships', 'id':id})
    return rend

def Revenue_consultancy_corporate_training_edit_display(request,id):
    obj = Revenue_consultancy_corporate_training.objects.get(pk=id)
    fm=Revenue_consultancy_corporate_training_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Revenue_consultancy_corporate_training_edit', 'heading': 'Revenue Consultancy Corporate Training', 'id':id})
    return rend

def Funds_provided_to_teacher_edit_display(request,id):
    obj= Funds_provided_to_teacher.objects.get(pk=id)
    fm=Funds_provided_to_teacher_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Funds_provided_to_teacher_edit', 'heading': 'Funds_provided_to_teacher', 'id':id})
    return rend

def Book_research_published_edit_display(request,id):
    obj= Book_research_published.objects.get(pk=id)
    fm=Book_research_published_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Book_research_published_edit', 'heading': 'Book_research_published', 'id':id})
    return rend

def E_content_devp_edit_display(request,id):
    obj= E_content_devp.objects.get(pk=id)
    fm=E_content_devp_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'E_content_devp_edit', 'heading': 'E_content_devp', 'id':id})
    return rend

def Faculty_dev_program_edit_display(request,id):
    obj= Faculty_dev_program.objects.get(pk=id)
    fm=Faculty_dev_program_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Faculty_dev_program_edit', 'heading': 'Faculty_dev_program', 'id':id})
    return rend


def Teacher_collaborative_activity_participation_edit_display(request,id):
    obj= Teacher_collaborative_activity_participation.objects.get(pk=id)
    fm=Teacher_collaborative_activity_participation_form(instance=obj)
    rend = render(request, 'institute/form_edit.html', {'form': fm, 'editurl': 'Teacher_collaborative_activity_participation_edit', 'heading': 'Teacher_collaborative_activity_participation', 'id':id})
    return rend

def Teacher_edit(request,id):
    obj = Teacher.objects.get(pk=id)
    fm = Teacher_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/admin_home')

def Award_fellowship_edit(request,id):
    obj = Award_fellowship.objects.get(pk=id)
    fm = Award_fellowship_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Revenue_consultancy_corporate_training_edit(request,id):
    obj = Revenue_consultancy_corporate_training.objects.get(pk=id)
    fm =Revenue_consultancy_corporate_training_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Funds_provided_to_teacher_edit(request,id):
    obj = Funds_provided_to_teacher.objects.get(pk=id)
    fm =Funds_provided_to_teacher_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Book_research_published_edit(request,id):
    obj = Book_research_published.objects.get(pk=id)
    fm =Book_research_published_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    else:
        return HttpResponse('Wrong Details')
    return HttpResponseRedirect('/teacher/home')

def E_content_devp_edit(request,id):
    obj = E_content_devp.objects.get(pk=id)
    fm =E_content_devp_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')


def Faculty_dev_program_edit(request,id):
    obj = Faculty_dev_program.objects.get(pk=id)
    fm =Faculty_dev_program_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Teacher_collaborative_activity_participation_edit(request,id):
    obj = Teacher_collaborative_activity_participation.objects.get(pk=id)
    fm =Teacher_collaborative_activity_participation_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/teacher/home')

def Teacher_bulk_upload(request):
    excelfile = request.FILES['file']
    wb = openpyxl.load_workbook(excelfile)
    ws = wb['Sheet1']
    rows = list(ws.rows)
    iter = 0
    for row in rows:
        if iter!=0:
            if not row[0].value:
                return HttpResponseRedirect('/institute/admin_home')
            user = User.objects.create_user(username=row[0].value, password=row[1].value, first_name=row[2].value,last_name=row[3].value, email=row[4].value)
            user.save()
            alluser = Alluser.objects.create(user=user, user_type='Teacher', mobile=row[5].value)
            alluser.save()
            teacher= Teacher.objects.create(teacher=alluser, pan_no=row[6].value, aadhar_no=row[7].value, designation=row[8].value,appointment_year=row[9].value, resignation_year=row[10].value, nature_of_appointment=row[11].value,experience=row[12].value, gender=row[13].value,present_status=row[14].value,qualifications=row[15].value, prog_id=row[16].value)
            teacher.save()
        iter = 1
    return HttpResponseRedirect('/institute/admin_home')



