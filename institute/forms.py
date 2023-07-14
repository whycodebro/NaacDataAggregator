from django.core import validators
from django import forms
from .models import *

class Program_form(forms.ModelForm):
    class Meta:
        model=Program
        fields= ['prog_code','prog_name','prog_type','year_of_intro','year_of_implementation','duration','cbcs_ecs_status','cbcs_ecs_year_implementation','prog_head_id']
        widgets= {
            'prog_code': forms.TextInput(attrs={'class':'form-control'}),
            'prog_name': forms.TextInput(attrs={'class':'form-control'}),
            'prog_type': forms.Select(choices=(('', '---'),('UG', 'UG'),('PG','PG'),), attrs={'class':'form-control'}),
            'year_of_intro': forms.NumberInput(attrs={'class':'form-control'}),
            'year_of_implementation': forms.NumberInput(attrs={'class':'form-control'}),
            'duration': forms.NumberInput(attrs={'class':'form-control'}),
            'cbcs_ecs_status': forms.Select(choices=(('', '---'),('yes', 'Yes'),('no','No'),), attrs={'class':'form-control'}),
            'cbcs_ecs_year_implementation':forms.NumberInput(attrs={'class':'form-control'}),
            'prog_head_id': forms.Select(attrs={'class':'form-control'}),
        }
        labels={'prog_code':'Program Code', 'prog_name':'Program Name', 'prog_type':'Program Type', 'year_of_intro':'Year of Introduction', 'year_of_implementation':'Year of Implementation', 'cbcs_ecs_status':'CBCS/ECS Status', 'cbcs_ecs_year_implementation':'CBCS/ECS Year of Implementation', 'prog_head_id':'Program Head'}

class Collaborative_activity_form(forms.ModelForm):
    class Meta:
        model= Collaborative_activity
        fields= ['title_of_activity','collaborating_agency_name','year_of_collaboration','duration','nature_of_activity','document_link']
        widgets={
            'title_of_activity': forms.TextInput(attrs={'class':'form-control'}),
            'collaborating_agency_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_collaboration': forms.NumberInput(attrs={'class':'form-control'}),
            'duration': forms.NumberInput(attrs={'class':'form-control'}),
            'nature_of_activity': forms.TextInput(attrs={'class':'form-control'}),
            'document_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'title_of_activity': 'Title of Activity', 'collaborating_agency_name':'Collaborating Agency Name', 'year_of_collaboration':'Year of Collaboration', 'nature_of_activity':'Nature of Activity','document_link':'Document Link'}

class Facility_dev_for_consultancy_form(forms.ModelForm):
    class Meta:
        model= Facility_dev_for_consultancy
        fields=['facility_developed_name','year_of_development','consultancy_name','amount_spend']
        widgets={
            'facility_developed_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_development': forms.NumberInput(attrs={'class':'form-control'}),
            'consultancy_name': forms.TextInput(attrs={'class':'form-control'}),
            'amount_spend': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'facility_developed_name': 'Facility Developed Name', 'year_of_development':'Year of Development','consultancy_name':'Consultancy Name','amount_spend':'Amount Spend' }

class Ict_facility_form(forms.ModelForm):
    class Meta:
        model= Ict_facility
        fields= ['program','room_number','facility_type','link_to_geo_tagged_photos']
        widgets={
            'program': forms.Select(attrs={'class':'form-control'}),
            'room_number': forms.TextInput(attrs={'class':'form-control'}),
            'facility_type': forms.TextInput(attrs={'class':'form-control'}),
            'link_to_geo_tagged_photos': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels= {'room_number':'Room Number','facility_type':'Facility Type','link_to_geo_tagged_photos': 'Link to Geo Tagged Photos' }

class Course_form(forms.ModelForm):
    class Meta:
        model= Course
        fields=['program','course_code','course_name','year_of_intro','course_duration']
        widgets={
            'program': forms.Select(attrs={'class':'form-control'}),
            'course_code': forms.TextInput(attrs={'class':'form-control'}),
            'course_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_intro': forms.NumberInput(attrs={'class':'form-control'}),
            'course_duration': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'course_code':'Course Code', 'course_name':'Course Name', 'year_of_intro':'Year of Introduction', 'course_duration':'Course Duration'}


class Students_enrolled_in_course_form(forms.ModelForm):
    class Meta:
        model= Students_enrolled_in_course
        fields=['course','year','number_of_students']
        widgets={
            'course': forms.Select(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_students': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'number_of_students':'Number of Students Enrolled'}

class Value_added_courses_form(forms.ModelForm):
    class Meta:
        model= Value_added_courses
        fields=['course','no_of_times_offered_in_a_year','number_of_students_completing_course','year']
        widgets={
            'course': forms.Select(attrs={'class':'form-control'}),
            'no_of_times_offered_in_a_year': forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_students_completing_course': forms.NumberInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'no_of_times_offered_in_a_year':'Number of Times offered', 'number_of_students_completing_course':'Number of Students Completing the Course'}

class Employbility_course_form(forms.ModelForm):
    class Meta:
        model= Employbility_course
        fields= ['course','activity_performed','document_link']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'activity_performed': forms.TextInput(attrs={'class':'form-control'}),
            'document_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {'activity_performed':'Activity Performed','document_link':'Document Link'}

class Category_seat_reservation_form(forms.ModelForm):
    class Meta:
        model= Category_seat_reservation
        fields=['program','category_type','number_of_seats_sanctioned','number_of_students_admitted','year']
        widgets={
            'program':forms.Select(attrs={'class': 'form-control'}),
            'category_type': forms.Select(choices=(('','---'),('General','GENERAL'),('OBC','OBC'),('SC','SC'),('ST','ST'),('PWD','PWD')),attrs={'class': 'form-control'}),
            'number_of_seats_sanctioned': forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_students_admitted': forms.NumberInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'category_type': 'Category Type', 'number_of_seats_sanctioned':'Number of Seats Sanctioned','number_of_students_admitted':'Number of Students Admitted'}

class Exam_result_form(forms.ModelForm):
    class Meta:
        model= Exam_result
        fields=['program','semester','year','exam_last_date','result_date','no_of_students_appeared','no_of_students_passed']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.NumberInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'exam_last_date': forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'result_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
            'no_of_students_appeared': forms.NumberInput(attrs={'class':'form-control'}),
            'no_of_students_passed': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'exam_last_date': 'Date of Last Exam', 'result_date': 'Date of Result'}

class Program_revision_form(forms.ModelForm):
    class Meta:
        model= Program_revision
        fields=['program','revision_year','percent_of_cont_modified','document_link']
        widgets={
            'program': forms.Select(attrs={'class': 'form-control'}),
            'revision_year': forms.NumberInput(attrs={'class':'form-control'}),
            'percent_of_cont_modified': forms.NumberInput(attrs={'class':'form-control'}),
            'document_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'revision_year':'Revision Year','percent_of_cont_modified':'Percent of Content Modified', 'document_link':'Document Link'}

class Mou_form(forms.ModelForm):
    class Meta:
        model= Mou
        fields= ['other_party_name','institute_name','year_of_signing','duration']
        widgets={
            'other_party_name': forms.TextInput(attrs={'class':'form-control'}),
            'institute_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_signing':forms.NumberInput(attrs={'class':'form-control'}),
            'duration':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'other_party_name':'Others Party Name', 'institute_name':'Institute Name', 'year_of_signing':'Year of Signing'}

class Mou_activity_form(forms.ModelForm):
    class Meta:
        model= Mou_activity
        fields=['mou','year','activity_title']
        widgets={
            'mou': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'activity_title': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'activity_title': 'Activity Title'}

class Workshop_seminar_form(forms.ModelForm):
    class Meta:
        model= Workshop_seminar
        fields=['name_of_workshop_seminar','year_of_conduction','no_of_participants','start_date','end_date','activity_report_link']
        widgets={
            'name_of_workshop_seminar': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_conduction': forms.NumberInput(attrs={'class':'form-control'}),
            'no_of_participants':forms.NumberInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
            'activity_report_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'name_of_workshop_seminar':'Name of Workshop Seminar', 'year_of_conduction':'Year od Conduction','no_of_participants':'Number of Participants', 'start_date':'Start Date','end_date':'End Date,','activity_report_link':'Activity Report Link'}

class Hei_guidence_activity_form(forms.ModelForm):
    class Meta:
        model= Hei_guidence_activity
        fields=['activity_name','year_of_conduction','number_of_students_enrolled','number_of_students_placed','document_link']
        widgets={
            'activity_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_conduction':forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_students_enrolled': forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_students_placed': forms.NumberInput(attrs={'class':'form-control'}),
            'document_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'activity_name':'Activity Name', 'year_of_conduction':'Year of Conduction','number_of_students_enrolled':'Number of Students Enrolled', 'number_of_students_placed':'Number of Students Placed', 'document_link':'Document Link'}

class Sports_cultural_event_by_intitution_form(forms.ModelForm):
    class Meta:
        model= Sports_cultural_event_by_intitution
        fields=['event_name','event_date']
        widgets={
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
        }
        labels={'event_name':'Event Name','event_date':'Event Date'}

class E_governance_form(forms.ModelForm):
    class Meta:
        model= E_governance
        fields=['type','implementation_year','doc_link']
        widgets={
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'implementation_year': forms.NumberInput(attrs={'class':'form-control'}),
            'doc_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'implementation_year':'Implementation Year', 'doc-link':'Document Link'}

class Extension_activity_award_form(forms.ModelForm):
    class Meta:
        model= Extension_activity_award
        fields=['activity_name','award_name','awarding_agency_name','year_of_awarding']
        widgets={
            'activity_name': forms.TextInput(attrs={'class':'form-control'}),
            'award_name': forms.TextInput(attrs={'class':'form-control'}),
            'awarding_agency_name': forms.TextInput(attrs={'class':'form-control'}),
            'year_of_awarding': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={'activity_name':'Activity Name', 'award_name':'Award Name','awarding_agency_name':'Awarding Agency Name', 'year_of_awarding':'Year of Awarding'}

class Funds_grants_to_inst_form(forms.ModelForm):
    class Meta:
        model= Funds_grants_to_inst
        fields=['ngo_name','grant_purpose','year','fund_amount','audit_doc_link']
        widgets={
            'ngo_name': forms.TextInput(attrs={'class':'form-control'}),
            'grant_purpose': forms.TextInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'fund_amount': forms.NumberInput(attrs={'class':'form-control'}),
            'audit_doc_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'ngo_name':'NGO Name','grant_purpose':'Grant Purpose','fund_amount':'Fund Amount','audit_doc_link':'Audit Document Link'}


class E_library_resource_form(forms.ModelForm):
    class Meta:
        model= E_library_resource
        fields=['type','subscription_details','subscription_expenditure','year','doc_link']
        widgets={
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'subscription_details': forms.TextInput(attrs={'class':'form-control'}),
            'subscription_expenditure': forms.NumberInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'doc_link': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'subscription_details':'Subscription Details', 'subscription_expenditure':'Subscription Expenditure', 'doc_link':'Document Link'}

class Prof_dev_skill_enhan_ext_outrch_prog_form(forms.ModelForm):
    class Meta:
        model=Prof_dev_skill_enhan_ext_outrch_prog
        fields=['program_title','start_date','end_date','no_of_participants','type','agency_or_organizing_unit','outrch_prog_scheme_name']
        widgets={
            'program_title': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}),
            'no_of_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'agency_or_organizing_unit': forms.TextInput(attrs={'class':'form-control'}),
            'outrch_prog_scheme_name': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'program_title':'Program Title', 'start_date':'Start Date','end_date':'End Date', 'no_of_participants':'Number of Participants', 'agency_or_organizing_unit':'Agency/Organizing Unit', 'outrch_prog_scheme_name':'Outreach Program Scheme Name'}

