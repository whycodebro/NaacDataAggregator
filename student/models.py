from django.db import models
from loginandregister.models import Alluser
from django.contrib.auth.models import User
from institute.models import Program,Collaborative_activity
# Create your models here.
class Student(models.Model):
    student= models.OneToOneField(Alluser,on_delete=models.CASCADE, primary_key=True)
    enroll_num= models.CharField(max_length=20)
    prog= models.ForeignKey(Program,null=True,on_delete=models.SET_NULL)
    gender= models.CharField(max_length=10)
    category= models.CharField(max_length=15)
    state_of_domicile= models.CharField(max_length=30)
    contact_number= models.CharField(max_length=10,null=True)
    year_of_admission= models.IntegerField()
    nationality= models.CharField(max_length=20)
    aadhar_no= models.CharField(max_length=12,null=True,blank=True)
    pan_no= models.CharField(max_length=10,null=True,blank=True)
    higher_sec_school_score_card_link= models.CharField(max_length=300,null=True,blank=True)
    higher_edu_inst_joined_name= models.CharField(max_length=100,null=True,blank=True)
    higher_edu_prog_name= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        user= User.objects.get(pk=self.student_id)
        return (self.enroll_num+'@'+str(user))



class Scholarship(models.Model):        #5.1.1, 5.1.2
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    year= models.IntegerField(null=True,blank=True)
    scheme_name= models.CharField(max_length=50, null=True, blank=True)
    amount= models.IntegerField(null=True, blank= True)
    scholarship_provider= models.CharField(max_length=50, null=True,blank=True)
    scheme_type= models.CharField(max_length=30,null=True,blank=True)
    doc_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.scheme_name+'@'+str(self.student)


class Placement_internship_project(models.Model):      #5.2.1, 1.3.4
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    year= models.IntegerField(null=True, blank=True)
    employer_name= models.CharField(max_length=50,null=True,blank=True)
    package= models.IntegerField(null=True,blank=True)
    internship_project_name= models.CharField(max_length=50,null=True,blank=True)
    document_link= models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return (str(self.student))


class Competative_exam(models.Model):   #5.2.3
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_year= models.IntegerField(null=True, blank=True)
    exam_name= models.CharField(max_length=50,null=True,blank=True)
    registration_number= models.CharField(max_length=50,null=True,blank=True)
    qualified_status= models.CharField(max_length=10, null=True,blank=True)
    name_of_institution_joined= models.CharField(max_length=100)
    program_admitted_to= models.CharField(max_length=50)
    def __str__(self):
        return (str(self.student)+'@'+self.exam_name)


class Sports_cultural_award(models.Model):  #5.3.1
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    year= models.IntegerField(null=True,blank=True)
    award_name= models.CharField(max_length=50,null=True,blank=True)
    team_name= models.CharField(max_length=30,null=True,blank=True)
    competition_type= models.CharField(max_length=20,null=True,blank=True)
    event_name= models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return (str(self.student)+'@'+self.award_name)

class Student_collaborative_activity_participation(models.Model):  #3.7.1
    activity= models.ForeignKey(Collaborative_activity,on_delete=models.CASCADE)
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.activity)+'@'+str(self.student))