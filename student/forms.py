from django.core import validators
from django import forms
from .models import *

STATE_CHOICES = (
   ("","---"),
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal"),
)
class Student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields= ['student','enroll_num','prog','gender','category','state_of_domicile','contact_number','year_of_admission','nationality','aadhar_no','pan_no','higher_sec_school_score_card_link','higher_edu_inst_joined_name','higher_edu_prog_name']
        widgets={
            'student':forms.Select(attrs={'class':'form-control'}),
            'enroll_num':forms.TextInput(attrs={'class':'form-control'}),
            'prog':forms.Select(attrs={'class':'form-control'}),
            'gender':forms.Select(choices=(('','---'),('male','Male'),('female','Female'),('other','Other'),),attrs={'class':'form-control'}),
            'category':forms.Select(choices=(('','---'),('General','General'),('OBC','OBC'),('EWS','EWS'),('ST','ST'),('SC','SC'),('PWD','PWD'),),attrs={'class':'form-control'}),
            'state_of_domicile':forms.Select(choices=STATE_CHOICES,attrs={'class':'form-control'}),
            'contact_number':forms.TextInput(attrs={'class':'form-control'}),
            'year_of_admission':forms. NumberInput(attrs={'class':'form-control'}),
            'nationality':forms.TextInput(attrs={'class':'form-control'}),
            'aadhar_no':forms.TextInput(attrs={'class':'form-control'}),
            'pan_no':forms.TextInput(attrs={'class':'form-control'}),
            'higher_sec_school_score_card_link':forms.TextInput(attrs={'class':'form-control'}),
            'higher_edu_inst_joined_name':forms.TextInput(attrs={'class':'form-control'}),
            'higher_edu_prog_name':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'student':'User','enroll_num':'Enrollment Number','prog':'Program','gender':'Gender','category':'Category','state_of_domicile':'State of Domicile','contact_number':'Contact Number','year_of_admission':'Year of Admission','nationality':'Nationality','aadhar_no':'Aadhar number','pan_no':'PAN Number','higher_sec_school_score_card_link':'Higher Sec School Score Card Link','higher_edu_inst_joined_name':'Higher Education Institution Joined Name','higher_edu_prog_name':'Higher Education Program Name'}
class Scholarship_form(forms.ModelForm):
    class Meta:
        model=Scholarship
        fields= ['student','year','scheme_name','amount','scholarship_provider','scheme_type','doc_link']
        widgets={
            'student':forms.HiddenInput(),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'scheme_name':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'scholarship_provider':forms.TextInput(attrs={'class':'form-control'}),
            'scheme_type':forms.TextInput(attrs={'class':'form-control'}),
            'doc_link':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'year':'Year','scheme_name':'Scheme Name','amount':'Amount','scholarship_provider':'Scholarship Provider','scheme_type':'Scheme Type','doc_link':'Doc Link'}
class Placement_internship_project_form(forms.ModelForm):
    class Meta:
        model= Placement_internship_project
        fields= ['student','year','employer_name','package','internship_project_name','document_link']
        widgets={
            'student': forms.HiddenInput(),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'employer_name':forms.TextInput(attrs={'class':'form-control'}),
            'package':forms.NumberInput(attrs={'class':'form-control'}),
            'internship_project_name':forms.TextInput(attrs={'class':'form-control'}),
            'document_link':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'year':'Year','employer_name':'Employer Name','internship_project_name':'Internship Project Name','document_link':'Document Link'}
class Competative_exam_form(forms.ModelForm):
    class Meta:
        model= Competative_exam
        fields=['student','exam_year','exam_name','registration_number','qualified_status','name_of_institution_joined','program_admitted_to']
        widgets={
            'student': forms.HiddenInput(),
            'exam_year':forms.NumberInput(attrs={'class':'form-control'}),
            'exam_name':forms.TextInput(attrs={'class':'form-control'}),
            'registration_number':forms.TextInput(attrs={'class':'form-control'}),
            'qualified_status':forms.TextInput(attrs={'class':'form-control'}),
            'name_of_institution_joined':forms.TextInput(attrs={'class':'form-control'}),
            'program_admitted_to':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'exam_year':'Exam Year','exam_name':'Exam Name','registration_number':'Registration Number','qualified_status':'Qualified Status','name_of_institution_joined':'Name Of Institution Joined','program_admitted_to':'Program Admitted To'}
class Sports_cultural_award_form(forms.ModelForm):
    class Meta:
        model= Sports_cultural_award
        fields=['student','year','award_name','team_name','competition_type','event_name']
        widgets={
            'student': forms.HiddenInput(),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'award_name':forms.TextInput(attrs={'class':'form-control'}),
            'team_name':forms.TextInput(attrs={'class':'form-control'}),
            'competition_type':forms.TextInput(attrs={'class':'form-control'}),
            'event_name':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'year':'Year','award_name':'Award Name','team_name':'Team Name','competition_type':'Competition Type','event_name':'Event Name'}

class Student_collaborative_activity_participation_form(forms.ModelForm):
    class Meta:
        model= Student_collaborative_activity_participation
        fields=['student','activity']
        widgets={
            'student': forms.HiddenInput(),
            'activity':forms.Select(attrs={'class':'form-control'}),
        }
        labels={'activity':'Activity'}