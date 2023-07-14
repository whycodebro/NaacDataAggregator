from django.shortcuts import render
from student import response_views
import xlwt
from django.http import HttpResponse,HttpResponseRedirect
from loginandregister.models import Alluser
from student.models import *
from student.forms import *
from django.contrib.auth.models import User
from django.db.models import Model
import openpyxl
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

def table1p3p4and1p3p4p1(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('1.3.4 and 1.3.4.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Program name')
    ws.write(0,1, 'Program Code')
    ws.write(0,2, 'Name of students undertaking field projects /internships/student projects')
    ws.write(0,3, 'Link to the relevant document')

    placement_list= Placement_internship_project.objects.all()
    row=1
    for obj in placement_list:
        ws.write(row, 0, obj.student.prog.prog_name)
        ws.write(row, 1, obj.student.prog.prog_code)
        ws.write(row, 2, obj.student.student.user.first_name+' '+obj.student.student.user.last_name)
        ws.write(row, 3, obj.document_link)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table2p7p1(request):  #not in database
    # Check db connection
    dict = getWorkbookAndWorksheet('2.7.1')
    wb = dict[workbook]
    ws = dict[worksheet]
    response = dict['response']
    ws.write(0, 0,'Name of the student')
    ws.write(0, 1, 'Gender')
    ws.write(0, 2, 'Category')
    ws.write(0, 3, 'State of Domicile')
    ws.write(0, 4, 'Nationality if othern than Indian')
    ws.write(0, 5, 'Email ID')
    ws.write(0, 6, 'Programme name')
    ws.write(0, 7, 'Student Unique Enrolment ID ')
    ws.write(0, 8, 'Mobile Number')
    ws.write(0, 9, 'Year of joining')

    wb.save(response)
    return response_views.excel_file_report(response)

def table5p1p1and5p1p2(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.1.1 and 5.1.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,1,1,1, 'Name of Scheme')
    ws.write_merge(0,0,2,3, 'Number of students benefited by government scheme and amount')
    ws.write(1,2,'Number of Students')
    ws.write(1,3,'Amount')
    ws.write_merge(0,1,5,5,'Link to Relevant Documnet')
    row=2
    gov_objs= Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='government' GROUP BY year,scheme_name,scheme_type;")
    for obj in gov_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        row=row+1
    row=row+3
    ws.write_merge(row,row+1,0,0,'Year')
    ws.write_merge(row,row+1, 1, 1, 'Name of Scheme')
    ws.write_merge(row, row, 2, 3, "Number of students benefited by intitution's scheme and amount")
    ws.write(row+1, 2, 'Number of Students')
    ws.write(row+1, 3, 'Amount')
    ws.write_merge(row, row+1, 5, 5, 'Link to Relevant Documnet')
    row=row+2
    inst_objs = Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='institute' GROUP BY year,scheme_name,scheme_type;")
    for obj in inst_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        row = row + 1
    row = row + 3
    ws.write_merge(row, row + 1, 0, 0, 'Year')
    ws.write_merge(row, row + 1, 1, 1, 'Name of Scheme')
    ws.write_merge(row, row, 2, 4, "Number of students benefited by non-government scheme and amount")
    ws.write(row + 1, 2, 'Number of Students')
    ws.write(row + 1, 3, 'Amount')
    ws.write(row + 1, 4, 'Agency name')
    ws.write_merge(row, row + 1, 5, 5, 'Link to Relevant Documnent')
    row = row + 2
    non_gov_objs = Scholarship.objects.raw("SELECT 1 as id,year,scheme_name,scheme_type,scholarship_provider,COUNT(*),SUM(amount) FROM public.student_scholarship WHERE scheme_type='non-government' GROUP BY year,scheme_name,scheme_type,scholarship_provider;")
    for obj in non_gov_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.scheme_name)
        ws.write(row, 2, obj.count)
        ws.write(row, 3, obj.sum)
        ws.write(row, 4, obj.scholarship_provider)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p1(request):
    #check database connectivity
    dict = getWorkbookAndWorksheet('5.2.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1,'Name of student placed')
    ws.write(0,2,'Program graduated from')
    ws.write(0,3,'Name of the employer')
    ws.write(0,4,'Pay package at appointment')
    data_list = Placement_internship_project.objects.all()
    row = 1
    for obj in data_list:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.student.student.user.first_name + ' ' + obj.student.student.user.last_name)
        ws.write(row, 2, obj.student.prog.prog_name)
        ws.write(row, 3, obj.employer_name)
        ws.write(row, 4, obj.package)
        row = row + 1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p2(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.2.2')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Name of student enrolling into higher education')
    ws.write(0,1, 'Program graduated from')
    ws.write(0,2, 'Name of institution joined')
    ws.write(0,3, 'Name of programme admitted to')
    row=1
    student_objs= Student.objects.raw("SELECT * FROM PUBLIC.student_student WHERE higher_edu_inst_joined_name IS NOT null")
    for obj in student_objs:
        ws.write(row,0, obj.student.user.first_name+' '+obj.student.user.last_name)
        ws.write(row,1, obj.prog.prog_name)
        ws.write(row,2, obj.higher_edu_inst_joined_name)
        ws.write(row,3, obj.higher_edu_prog_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p2p3(request): #pending
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.2.3')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write_merge(0,1,0,0,'Year')
    ws.write_merge(0,1,1,1,'Registration number/roll number for the exam')
    ws.write_merge(0,1,2,2, 'Names of students selected/ qualified')
    ws.write_merge(0, 0, 3, 14, 'Examination Qualified')
    ws.write(1, 3, 'NET')
    ws.write(1, 4, 'SLET')
    ws.write(1, 5, 'GATE')
    ws.write(1, 6, 'GMAT')
    ws.write(1, 7, 'CAT')
    ws.write(1, 8, 'GRE')
    ws.write(1, 9, 'JAM')
    ws.write(1, 10, 'IELTS')
    ws.write(1, 11, 'TOEFL')
    ws.write(1, 12, 'Civil Services')
    ws.write(1, 13, 'State government examinations')
    ws.write(1, 14, 'Other examinations conducted by the State / Central Government Agencies (Specify)')
    wb.save(response)
    return response_views.excel_file_report(response)

def table5p3p1(request):
    # Check database connectivity
    dict = getWorkbookAndWorksheet('5.3.1')
    wb = dict['wb']
    ws = dict['ws']
    response = dict['response']
    ws.write(0,0,'Year')
    ws.write(0,1, 'Name of the award/ medal')
    ws.write(0,2, 'Team / Individual')
    ws.write(0,3, 'inter-university / state /  National/ International')
    ws.write(0,4, 'Name of the event')
    ws.write(0,5, 'Name of the student')
    sports_objs= Sports_cultural_award.objects.all()
    row=1
    for obj in sports_objs:
        ws.write(row, 0, obj.year)
        ws.write(row, 1, obj.award_name)
        ws.write(row, 2, obj.team_name)
        ws.write(row, 3, obj.competition_type)
        ws.write(row, 4, obj.event_name)
        ws.write(row, 5, obj.student.student.user.first_name+' '+obj.student.student.user.first_name)
        row=row+1
    wb.save(response)
    return response_views.excel_file_report(response)


def displayhomestudent(request):
    #Database connectivity and data fetch
    user = request.user
    alluser = Alluser.objects.get(user=user)
    student = Student.objects.get(student=alluser)
    dict_list=[Scholarship_display(request),Placement_internship_project_display(request),Competative_exam_display(request),Sports_cultural_award_display(request),Student_collaborative_activity_participation_display(request)]
    dict= {'alluser':alluser, 'student':student, 'dict_list':dict_list}
    return response_views.htmlpage(request, 'student/home.html', dict)


def displayacademicinfo(request):
    #Database connectivity and data fetch
    return response_views.htmlpage(request, 'student/details.html', {})

def Student_display(request):
    stu_list = Student.objects.all()
    heading_list = ['student','enroll_num', 'prog', 'gender', 'category']  # Imp
    alt_heading_list = ['Student','Enrollment Number', 'Program', 'Gender', 'Category']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['prog'] = stu.prog  # Imp
        dict['student']= stu.student
        newdict = {}  # Imp
        newdict['unique_id'] = stu.student_id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Student_form()  # Imp

    temp_dict = {'table_name':'Students','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Student_edit_display',
                 'deleteurl': 'Student_delete', 'form': fm,'bulkaddurl':'Student_bulk_upload',}
    return temp_dict

def Scholarship_display(request):
    alluser=Alluser.objects.get(user=request.user)
    student = None
    if alluser.user_type == 'Student':
        student = Student.objects.get(student=alluser)
    stu_list = Scholarship.objects.filter(student=student)
    heading_list = ['year', 'scheme_name', 'amount', 'scholarship_provider','scheme_type']  # Imp
    alt_heading_list = ['Year', 'Scheme Name', 'Amount', 'Scholarship Provider','Scheme Type']  # Imp
    if alluser.user_type!='Student':
        stu_list = Scholarship.objects.all()
        heading_list.append('student')
        alt_heading_list.append('Student')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['student'] = stu.student

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name':'Scholarships','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Scholarship_edit_display',
                 'deleteurl': 'Scholarship_delete','addurl':'Scholarship_add_display'}
    if alluser.user_type != 'Student':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''

    return temp_dict

def Placement_internship_project_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student=None
    if alluser.user_type=='Student':
        student = Student.objects.get(student=alluser)
    stu_list = Placement_internship_project.objects.filter(student=student)
    heading_list = ['year', 'employer_name', 'package', 'internship_project_name']  # Imp
    alt_heading_list = ['Year', 'Employer Name', 'Package', 'Internship Project Name ']  # Imp
    if alluser.user_type!='Student':
        stu_list = Placement_internship_project.objects.all()
        heading_list.append('student')
        alt_heading_list.append('Student')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
      # Imp
        dict['student']= stu.student
        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name':'Placement/Internship Projects','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Placement_internship_project_edit_display',
                 'deleteurl': 'Placement_internship_project_delete','addurl':'Placement_internship_project_add_display'}
    if alluser.user_type != 'Student':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''

    return temp_dict

def Competative_exam_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = None
    if alluser.user_type == 'Student':
        student = Student.objects.get(student=alluser)
    stu_list = Competative_exam.objects.filter(student=student)
    heading_list = ['exam_year', 'exam_name', 'registration_number', 'qualified_status','name_of_institution_joined','program_admitted_to']  # Imp
    alt_heading_list = ['Exam Year', 'Exam Name', 'Registration Number', 'Qualified Status','Name Of Institution Joined','Program Admitted To']  # Imp
    if alluser.user_type!='Student':
        stu_list = Competative_exam.objects.all()
        heading_list.append('student')
        alt_heading_list.append('Student')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['student']=stu.student

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name':'Competative Exam','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Competative_exam_edit_display',
                 'deleteurl': 'Competative_exam_delete', 'addurl':'Competative_exam_add_display'}
    if alluser.user_type != 'Student':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict

def Sports_cultural_award_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = None
    if alluser.user_type == 'Student':
        student = Student.objects.get(student=alluser)
    stu_list = Sports_cultural_award.objects.filter(student=student)
    heading_list = ['year', 'award_name', 'team_name', 'competition_type','event_name']  # Imp
    alt_heading_list = ['Year', 'Award Name', 'Team Name', 'Competition Type','Event Name']  # Imp
    if alluser.user_type!='Student':
        stu_list = Sports_cultural_award.objects.all()
        heading_list.append('student')
        alt_heading_list.append('Student')
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['student'] = stu.student

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp

    temp_dict = {'table_name':'Sports Cultural Award','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Sports_cultural_award_edit_display',
                 'deleteurl': 'Sports_cultural_award_delete','addurl':'Sports_cultural_award_add_display'}
    if alluser.user_type != 'Student':
        temp_dict['editurl']=''
        temp_dict['deleteurl']=''
        temp_dict['addurl']=''
    return temp_dict

def Student_collaborative_activity_participation_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    stu_list = Student_collaborative_activity_participation.objects.filter(student=student)
    heading_list = ['activity']  # Imp
    alt_heading_list = ['Activity']  # Imp
    obj_list = []  # Imp
    for stu in stu_list:
        dict = vars(stu)
        dict['activity'] = stu.activity # Imp

        newdict = {}  # Imp
        newdict['unique_id'] = stu.id  # Imp
        for hd in heading_list:  # Imp
            newdict[hd] = dict[hd]  # Imp
        obj_list.append(newdict)  # Imp
    fm = Student_collaborative_activity_participation_form(initial={'student':student})  # Imp

    temp_dict = {'table_name':'Student Collaborative Activity Participation','Heading_add_entry': 'Add New Entry', 'Heading_show_entry': 'Records', 'obj_list': obj_list,
                 'heading_list': heading_list, 'alt_heading_list': alt_heading_list, 'editurl': 'Student_collaborative_activity_participation_edit_display',
                 'deleteurl': 'Student_collaborative_activity_participation_delete', 'form': fm,'addurl':'Student_collaborative_activity_participation_add_display'}
    return temp_dict

def student_tables(request):
    table_dict={
        'Scholarships':'/student/Scholarship',
        'Placement/Internship Projects':'/student/Placement_internship_project',
        'Competative Exams':'/student/Competative_exam',
        'Sports/Cultural Awards':'/student/Sports_cultural_award',
        'Collaborative Activities': '/student/Student_collaborative_activity_participation',
    }
    rend= render(request,'institute/tables.html', {'table_dict':table_dict})
    return rend

def Student_delete(request, id):
    student = Student.objects.get(pk=id)
    alluser = student.student
    user = alluser.user
    user.delete()
    return HttpResponseRedirect('/institute/admin_home')

def Scholarship_delete(request,id):
    obj= Scholarship.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/student/home/')

def Placement_internship_project_delete(request,id):
    obj= Placement_internship_project.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/student/home')


def Competative_exam_delete(request,id):
    obj= Competative_exam.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/student/home')



def Sports_cultural_award_delete(request,id):
    obj= Sports_cultural_award.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/student/home')

def Student_collaborative_activity_participation_delete(request,id):
    obj= Student_collaborative_activity_participation.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/student/home')

def Student_add(request):
    fm= Student_form(request.POST)
    if fm.is_valid():
        fm.save()
    else:
        fm=Student_form()
    return HttpResponseRedirect('/student/home')

def Scholarship_add(request):
    fm= Scholarship_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Placement_internship_project_add(request):
    fm= Placement_internship_project_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Competative_exam_add(request):
    fm= Competative_exam_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Sports_cultural_award_add(request):
    fm= Sports_cultural_award_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Student_collaborative_activity_participation_add(request):
    fm= Student_collaborative_activity_participation_form(request.POST)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')



def Scholarship_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    fm=Scholarship_form(initial={'student':student})
    rend= render(request, 'institute/form.html',{'form':fm,'addurl':'Scholarship_add','heading':'Scholarships'})
    return rend

def Placement_internship_project_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    fm=Placement_internship_project_form(initial={'student':student})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Placement_internship_project_add', 'heading': 'Placement/Internship Projects'})
    return rend


def Competative_exam_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    fm=Competative_exam_form(initial={'student':student})
    rend = render(request, 'institute/form.html', {'form': fm, 'addurl': 'Competative_exam_add', 'heading': 'Competative Exams'})
    return rend

def Sports_cultural_award_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    fm= Sports_cultural_award_form(initial={'student':student})
    rend = render(request, 'institute/form.html',
                  {'form': fm, 'addurl': 'Sports_cultural_award_add', 'heading': 'Sports Cultural Award'})
    return rend

def Student_collaborative_activity_participation_add_display(request):
    alluser = Alluser.objects.get(user=request.user)
    student = Student.objects.get(student=alluser)
    fm=Student_collaborative_activity_participation_form(initial={'student':student})
    rend= render(request, 'institute/form.html', {'form': fm, 'addurl': 'Student_collaborative_activity_participation_add', 'heading': 'Student Collaborative Activity Participation'})
    return rend

def Student_edit_display(request,id):
    obj = Student.objects.get(pk=id)
    fm = Student_form(instance=obj)
    return render(request, 'institute/form_edit.html',
                  {'form': fm, 'editurl': 'Student_edit', 'heading': 'Students', 'id': id})

def Scholarship_edit_display(request,id):
    obj= Scholarship.objects.get(pk=id)
    fm= Scholarship_form(instance=obj)
    return render(request,'institute/form_edit.html', {'form':fm, 'editurl': 'Scholarship_edit', 'heading': 'Scholarships', 'id':id})

def Placement_internship_project_edit_display(request,id):
    obj= Placement_internship_project.objects.get(pk=id)
    fm= Placement_internship_project_form(instance=obj)
    return render(request,'institute/form_edit.html', {'form':fm, 'editurl': 'Placement_internship_project_edit', 'heading': 'Placement/Internship Projects', 'id':id})

def Competative_exam_edit_display(request,id):
    obj= Competative_exam.objects.get(pk=id)
    fm= Competative_exam_form(instance=obj)
    return render(request,'institute/form_edit.html', {'form':fm, 'editurl': 'Competative_exam_edit', 'heading': 'Competative Exams', 'id':id})

def Sports_cultural_award_edit_display(request,id):
    obj= Sports_cultural_award.objects.get(pk=id)
    fm= Sports_cultural_award_form(instance=obj)
    return render(request,'institute/form_edit.html', {'form':fm, 'editurl': 'Sports_cultural_award_edit', 'heading': 'Sports/Cultural Awards', 'id':id})

def Student_collaborative_activity_participation_edit_display(request,id):
    obj= Student_collaborative_activity_participation.objects.get(pk=id)
    fm= Student_collaborative_activity_participation_form(instance=obj)
    return render(request,'institute/form_edit.html', {'form':fm, 'editurl': 'Student_collaborative_activity_participation_edit', 'heading': 'Student Collaborative Activity Participation', 'id':id})

def Student_edit(request,id):
    obj = Student.objects.get(pk=id)
    fm = Student_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/institute/admin_home')

def Scholarship_edit(request,id):
    obj=Scholarship.objects.get(pk=id)
    fm= Scholarship_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Placement_internship_project_edit(request,id):
    obj=Placement_internship_project.objects.get(pk=id)
    fm= Placement_internship_project_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Competative_exam_edit(request,id):
    obj=Competative_exam.objects.get(pk=id)
    fm= Competative_exam_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Sports_cultural_award_edit(request,id):
    obj=Sports_cultural_award.objects.get(pk=id)
    fm= Sports_cultural_award_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Student_collaborative_activity_participation_edit(request,id):
    obj=Student_collaborative_activity_participation.objects.get(pk=id)
    fm= Student_collaborative_activity_participation_form(request.POST, instance=obj)
    if fm.is_valid():
        fm.save()
    return HttpResponseRedirect('/student/home')

def Student_bulk_upload(request):
    excelfile= request.FILES['file']
    wb= openpyxl.load_workbook(excelfile)
    ws= wb['Sheet1']
    rows= list(ws.rows)
    iter= 0
    for row in rows:
        if iter!=0:
            if not row[0].value:
                return HttpResponseRedirect('/institute/admin_home')
            user=User.objects.create_user(username=row[0].value, password=row[1].value, first_name=row[2].value, last_name=row[3].value, email=row[4].value)
            user.save()
            alluser= Alluser.objects.create(user=user, user_type='Student', mobile=row[5].value)
            alluser.save()
            student= Student.objects.create(student=alluser,enroll_num=row[6].value, gender=row[7].value, category=row[8].value, state_of_domicile=row[9].value, year_of_admission=row[10].value, nationality=row[11].value, aadhar_no=row[12].value,pan_no=row[13].value, higher_sec_school_score_card_link=row[14].value, higher_edu_inst_joined_name=row[15].value,higher_edu_prog_name=row[16].value, prog_id=row[17].value,contact_number=row[5].value)
            student.save()
        iter=1
    return HttpResponseRedirect('/institute/admin_home')

