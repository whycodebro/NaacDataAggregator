from django.shortcuts import render
from student.models import Student
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from student.forms import *
def displayhomepage(request):
    stu_list=Student.objects.all()
    heading_list = ['enroll_num', 'prog', 'gender', 'category']   #Imp
    alt_heading_list= ['Enrollment Number', 'Program', 'Gender', 'Category']  #Imp
    obj_list=[]  #Imp
    for stu in stu_list:
        dict=vars(stu)
        dict['prog']=stu.prog  #Imp

        newdict={}  #Imp
        newdict['unique_id']=stu.student_id #Imp
        for hd in heading_list:  #Imp
            newdict[hd]=dict[hd]  #Imp
        obj_list.append(newdict)  #Imp
    fm=Student_collaborative_activity_participation_form() #Imp

    temp_dict={'Heading_add_entry':'Add New Entry','Heading_show_entry':'Records','obj_list':obj_list, 'heading_list':heading_list, 'alt_heading_list': alt_heading_list,'editurl':'edit_entry', 'deleteurl':'delete_entry','form':fm}
    rend= render(request,'institute/crud.html', temp_dict)
    return rend

def delete_entry(request,id):
    student= Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect('/samplereportgen/')

def edit_entry(request,id):
    print("id"+id+"edited")