from django.db import models
from loginandregister.models import Alluser
from django.contrib.auth.models import User
from institute.models import Program,Collaborative_activity
# Create your models here.
class Teacher(models.Model):
    teacher= models.OneToOneField(Alluser,on_delete=models.CASCADE, primary_key=True)
    pan_no=  models.CharField(max_length=10,null=True,blank=True)
    aadhar_no = models.CharField(max_length=12, null=True, blank=True)
    prog = models.ForeignKey(Program, null=True,on_delete=models.SET_NULL)
    designation= models.CharField(max_length=20,blank=True,null=True)
    appointment_year= models.IntegerField(null=True,blank=True)
    resignation_year= models.IntegerField(null=True,blank=True)
    nature_of_appointment= models.CharField(max_length=20,blank=True)
    experience= models.IntegerField(null=True,blank=True)
    contact_number= models.CharField(max_length=10,null=True,blank=True)
    gender = models.CharField(max_length=10)
    present_status= models.CharField(max_length=20,null=True,blank=True)
    qualifications= models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        user= User.objects.get(pk=self.teacher_id)
        return str(user.first_name+" "+user.last_name+" "+user.username)

class Award_fellowship(models.Model):   #3.1.3
    teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)
    award_fellowship_name= models.CharField(max_length=50, null=True, blank=True)
    award_year= models.IntegerField(null=True, blank=True)
    awarding_agency= models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return (str(self.teacher)+'@'+self.award_fellowship_name)

class Revenue_consultancy_corporate_training(models.Model):     #3.5.1
    teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)
    type= models.CharField(max_length=20, null=True,blank=True)
    title= models.CharField(max_length=50,null=True,blank=True)
    consulting_sponsoring_agency_name= models.CharField(max_length=50,null=True,blank=True)
    contact_details= models.CharField(max_length=100, null=True, blank=True)
    year= models.IntegerField(null=True, blank=True)
    revenue_generated= models.IntegerField(null=True,blank=True)
    number_of_trainee= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return (str(self.teacher)+'@'+self.title)


class Funds_provided_to_teacher(models.Model):  #3.5.2, 1.2.6, 6.3.2
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    agency_name= models.CharField(max_length=50,null=True,blank=True)
    year= models.IntegerField(null=True,blank=True)
    name_of_cons_or_research_or_conf= models.CharField(max_length=50,null=True,blank=True)
    amount_spend= models.IntegerField(null=True,blank=True)
    type= models.CharField(max_length=20, blank=True, null=True)
    policy_doc_link= models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return (str(self.teacher)+'@'+self.name_of_cons_or_research_or_conf)


class Book_research_published(models.Model):    #3.4.3, 3.4.4
    teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE)
    book_chapter_title= models.CharField(max_length=50, null=True, blank= True)
    author_name= models.CharField(max_length=50, null=True, blank= True, default=None)
    publication_year= models.IntegerField(null=True,blank=True)
    publisher_journal_name= models.CharField(max_length=100, null=True, blank=True)
    type_of_publish= models.CharField(max_length= 20, null=True, blank=True)
    publish_title= models.CharField(max_length=50,null=True,blank=True)
    isbn_issn_number= models.CharField(max_length=50, null=True,blank=True)
    institution_name_during_publication= models.CharField(max_length=100, null=True,blank=True)
    listed_in_ugc_status= models.CharField(max_length=10, null=True,blank=True)
    journal_website_link= models.CharField(max_length=300, null=True, blank=True)
    doc_link= models.CharField(max_length=300,null=True,blank=True)
    is_listed_in_ugc_care_scopus= models.CharField(max_length=10, null=True,blank=True)
    def __str__(self):
        return (str(self.teacher)+'@'+str(self.publish_title))


class E_content_devp(models.Model):     #4.3.4
    teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE)
    module_name= models.CharField(max_length=50,null=True,blank=True)
    platform_name= models.CharField(max_length=50,null=True,blank=True)
    date_of_launch= models.DateField(null=True,blank=True)
    doc_link= models.CharField(max_length=300,null=True,blank=True)
    type= models.CharField(max_length=20,null=True,blank=True)
    playlist_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return (str(self.teacher) + '@' + self.module_name)


class Faculty_dev_program(models.Model):   #6.3.4
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    program_title= models.CharField(max_length=50,null=True,blank=True)
    start_date= models.DateField(null=True,blank=True)
    end_date= models.DateField(null=True,blank=True)
    def __str__(self):
        return (str(self.teacher) + '@' + self.program_title)

class Teacher_collaborative_activity_participation(models.Model):   #3.7.1
    activity = models.ForeignKey(Collaborative_activity, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.activity) + '@' + str(self.teacher))

