from django.core import validators
from django import forms
from .models import *

class Teacher_form(forms.ModelForm):
    class Meta:
        model= Teacher
        fields= ['teacher','pan_no','aadhar_no','prog','designation','appointment_year','resignation_year','nature_of_appointment','experience','contact_number','gender','present_status','qualifications']
        widgets= {
                    'teacher': forms.Select(attrs={'class':'form-control'}),
                    'pan_no': forms.TextInput(attrs={'class':'form-control'}),
                    'aadhar_no': forms.TextInput(attrs={'class':'form-control'}),
                    'prog': forms.Select(choices=(('', '---'),('UG', 'UG'),('PG','PG'),), attrs={'class':'form-control'}),
                    'designation': forms.TextInput(attrs={'class':'form-control'}),
                    'appointment_year': forms.NumberInput(attrs={'class':'form-control'}),
                    'resignation_year': forms.NumberInput(attrs={'class':'form-control'}),
                    'nature_of_appointment':forms.TextInput(attrs={'class':'form-control'}),
                    'experience': forms.NumberInput(attrs={'class':'form-control'}),
                    'contact_number': forms.NumberInput(attrs={'class':'form-control'}),
                    'gender':forms.Select(choices=(('', '---'),('Male', 'MALE'),('Female','FEMALE'),('Other', 'OTHERS')), attrs={'class':'form-control'}),
                    'present_status': forms.TextInput(attrs={'class':'form-control'}),
                    'qualifications': forms.TextInput(attrs={'class':'form-control'}),
                }
        labels={'teacher':'User','pan_no':'Pan No.', 'aadhar_no':'Aadhar No.', 'prog':'Program', 'designation':'Designation', 'appointment_year':'Appointment Year', 'resignation_year':'Resignation Year', 'nature_of_appointment':'Nature Of Appointment', 'experience':'Experience', 'contact_number':'Contact Number', 'gender':'Gender', 'present_status':'Present Status', 'qualifications':'Qualifications'}


class Award_fellowship_form(forms.ModelForm):
    class Meta:
        model=Award_fellowship
        fields= ['teacher','award_fellowship_name','award_year','awarding_agency']
        widgets= {
                    'teacher':forms.HiddenInput(),
                     'award_fellowship_name': forms.TextInput(attrs={'class':'form-control'}),
                     'award_year': forms.NumberInput(attrs={'class':'form-control'}),
                     'awarding_agency': forms.TextInput(attrs={'class':'form-control'}),

                  }
        labels={'award_fellowship_name':'Award Fellowship Name', 'award_year':'Award Year', 'awarding_agency':'Awarding Agency',}


class Revenue_consultancy_corporate_training_form(forms.ModelForm):
    class Meta:
        model=Revenue_consultancy_corporate_training
        fields= ['teacher','type','title','consulting_sponsoring_agency_name','contact_details','year','revenue_generated','number_of_trainee','revenue_generated','number_of_trainee']
        widgets= {
            'teacher': forms.HiddenInput(),
                        'type': forms.TextInput(attrs={'class':'form-control'}),
                        'title': forms.TextInput(attrs={'class':'form-control'}),
                        'consulting_sponsoring_agency_name': forms.TextInput(attrs={'class':'form-control'}),
                        'contact_details': forms.TextInput(attrs={'class':'form-control'}),
                        'year': forms.NumberInput(attrs={'class':'form-control'}),
                        'revenue_generated':forms.NumberInput(attrs={'class':'form-control'}),
                        'number_of_trainee':forms.NumberInput(attrs={'class':'form-control'}),
                 }
        labels={'type': 'Type', 'title':'Title', 'consulting_sponsoring_agency_name':'Consulting/Sponsoring Agency','contact_details':'Contact Details','revenue_generated':'Revenue Generated', 'number_of_traniee':'Number of Trainee'}


class Funds_provided_to_teacher_form(forms.ModelForm):
    class Meta:
        model=Funds_provided_to_teacher
        fields= ['teacher','agency_name','year','name_of_cons_or_research_or_conf','amount_spend','type','policy_doc_link']
        widgets= {
            'teacher': forms.HiddenInput(),
                            'agency_name': forms.TextInput(attrs={'class':'form-control'}),
                            'year': forms.NumberInput(attrs={'class':'form-control'}),
                            'name_of_cons_or_research_or_conf': forms.TextInput(attrs={'class':'form-control'}),
                            'amount_spend': forms.NumberInput(attrs={'class':'form-control'}),
                            'type': forms.TextInput(attrs={'class':'form-control'}),
                            'policy_doc_link': forms.TextInput(attrs={'class':'form-control'}),
                        }
        labels={'agency_name':'Agency Name','name_of_cons_or_research_or_conf':'Name of Cons or Research or Conf','amount_spend':'Amount Spend', 'policy_doc_link':'Policy Document Link'}


class Book_research_published_form(forms.ModelForm):
    class Meta:
        model=Book_research_published
        fields= ['teacher','book_chapter_title','author_name','publication_year','publisher_journal_name','type_of_publish','publish_title','isbn_issn_number','institution_name_during_publication','listed_in_ugc_status','journal_website_link','doc_link','is_listed_in_ugc_care_scopus']
        widgets= {
                    'teacher': forms.HiddenInput(),
                    'book_chapter_title': forms.TextInput(attrs={'class':'form-control'}),
                    'author_name': forms.TextInput(attrs={'class':'form-control'}),
                    'publication_year': forms.NumberInput(attrs={'class':'form-control'}),
                    'publisher_journal_name': forms.TextInput(attrs={'class':'form-control'}),
                    'type_of_publish': forms.TextInput(attrs={'class':'form-control'}),
                    'publish_title': forms.TextInput(attrs={'class':'form-control'}),
                    'isbn_issn_number':forms.TextInput(attrs={'class':'form-control'}),
                    'institution_name_during_publication': forms.TextInput(attrs={'class':'form-control'}),
                    'listed_in_ugc_status': forms.TextInput(attrs={'class':'form-control'}),
                    'journal_website_link':forms.TextInput(attrs={'class':'form-control'}),
                    'doc_link': forms.TextInput(attrs={'class':'form-control'}),
                    'is_listed_in_ugc_care_scopus': forms.TextInput(attrs={'class':'form-control'}),
                }
        labels={'book_chapter_title':'Book Chapter Title','author_name':'Author Name','publication_year':'Year Of Publication','publisher_journal_name':'Name Of Publisher Journal','type_of_publish':'Type Of Publish','publish_title':'Title Of Publish','isbn_issn_number':'ISBN ISSN Nummber','institution_name_during_publication':'Name Of Institution During Publication','listed_in_ugc_status':'Listed in UGC status','journal_website_link':'Journal Website Link','doc_link':'Document Link','is_listed_in_ugc_care_scopus':'Is Listed In UGC Care Scopus'}
                    


class E_content_devp_form(forms.ModelForm):
    class Meta:
        model=E_content_devp
        fields= ['teacher','module_name','platform_name','date_of_launch','doc_link','type','playlist_link']
        widgets = {
            'teacher': forms.HiddenInput(),
            'module_name': forms.TextInput(attrs={'class':'form-control'}),
            'platform_name'  : forms.TextInput(attrs={'class':'form-control'}),
            'date_of_launch' : forms.DateInput(attrs={'class':'form-control'}),
            'doc_link' : forms.TextInput(attrs={'class':'form-control'}),
            'type' : forms.TextInput(attrs={'class':'form-control'}),
            'playlist_link' : forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'platform_name':'Platform Name','date_of_launch':'Date Of Launch','doc_link':'Document Link','type':'Type','playlist_link':'Playlist Link'}



class Faculty_dev_program_form(forms.ModelForm):
    class Meta:
        model=Faculty_dev_program
        fields= ['teacher','program_title','start_date','end_date']
        widgets = {
            'teacher': forms.HiddenInput(),
            'program_title'  : forms.TextInput(attrs={'class':'form-control'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control'}),
            'end_date' : forms.DateInput(attrs={'class':'form-control'}),
        }
        labels={'program_title':'Program','start_date':'Start Date','end_date':'End Date'}




class Teacher_collaborative_activity_participation_form(forms.ModelForm):
    class Meta:
        model=Teacher_collaborative_activity_participation
        fields= ['teacher','activity']
        widgets = {
            'activity' : forms.Select(attrs={'class':'form-control'}),
            'teacher'  : forms.HiddenInput()
        }
        labels={'activity':'Activity'}