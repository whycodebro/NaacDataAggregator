from django.db import models
from loginandregister.models import Alluser
from django.contrib.auth.models import User
# Create your models here.
class Program(models.Model):
    prog_id=models.IntegerField(primary_key=True)
    prog_code= models.CharField(max_length=30)
    prog_name= models.CharField(max_length=50)
    prog_type= models.CharField(max_length=20)
    year_of_intro= models.IntegerField(null=True)
    year_of_implementation= models.IntegerField(null=True)
    duration=models.IntegerField(null=True)
    cbcs_ecs_status=models.CharField(max_length=10)
    cbcs_ecs_year_implementation= models.IntegerField(null=True)
    prog_head_id= models.ForeignKey(Alluser,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return (self.prog_name+'@'+self.prog_type)

class Collaborative_activity(models.Model):     #3.7.1
    title_of_activity=models.CharField(max_length=50,null=True,blank=True)
    collaborating_agency_name= models.CharField(max_length=50,null=True,blank=True)
    year_of_collaboration= models.IntegerField(null=True,blank=True)
    duration= models.IntegerField(null=True,blank=True)
    nature_of_activity= models.CharField(max_length=30)
    document_link= models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.title_of_activity

class Facility_dev_for_consultancy(models.Model):   #3.5.2
    facility_developed_name= models.CharField(max_length=100, null=True, blank=True)
    year_of_development= models.IntegerField(null=True,blank=True)
    consultancy_name= models.CharField(max_length=50, null=True, blank=True)
    amount_spend= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return (self.facility_developed_name)

class Ict_facility(models.Model):   #4.1.3
    program= models.ForeignKey(Program,on_delete=models.CASCADE)
    room_number= models.CharField(max_length=15,null=True,blank=True)
    facility_type= models.CharField(max_length=20,null=True,blank=True)
    link_to_geo_tagged_photos= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        prog= Program.objects.get(pk=self.program_id)
        return (str(prog)+'@'+self.facility_type)

class Course(models.Model):
    program= models.ForeignKey(Program,on_delete=models.CASCADE)
    course_code= models.CharField(max_length=20, null=True, blank=True)
    course_name= models.CharField(max_length=30, null=True, blank=True)
    year_of_intro= models.IntegerField(null=True,blank=True)
    course_duration= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.course_name

class Students_enrolled_in_course(models.Model):
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    year= models.IntegerField(null=True,blank=True)
    number_of_students= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.course)

class Value_added_courses(models.Model):  #1.3.2, 1.3.3
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    no_of_times_offered_in_a_year= models.IntegerField(null=True, blank=False)
    number_of_students_completing_course= models.IntegerField(null=True,blank=True)
    year= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.course)

class Employbility_course(models.Model):  #1.1.3, 1.2.1
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    activity_performed= models.CharField(max_length=50,null=True,blank=True)
    document_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return str(self.course)

class Category_seat_reservation(models.Model): #2.1.1, 2.1.2
    program= models.ForeignKey(Program,on_delete=models.CASCADE)
    category_type=models.CharField(max_length=20, blank=True, null=True)
    number_of_seats_sanctioned= models.IntegerField(null=True)
    number_of_students_admitted= models.IntegerField(null=True)
    year= models.IntegerField(null=True)
    def __str__(self):
        prog= Program.objects.get(pk=self.program_id)
        return (self.category_type+'@'+prog.prog_name+'@'+prog.prog_type)

class Exam_result(models.Model):  #2.5.1, 2.6.3
    program= models.ForeignKey(Program,on_delete=models.CASCADE)
    semester= models.IntegerField(null=True,blank=True)
    year= models.IntegerField(null=True,blank=True)
    exam_last_date= models.DateField(null=True,blank=True)
    result_date= models.DateField(null=True,blank=True)
    no_of_students_appeared=models.IntegerField(null=True,blank=True)
    no_of_students_passed=models.IntegerField(null=True,blank=True)
    def __str__(self):
        prog= Program.objects.get(pk=self.program_id)
        return (prog.prog_name+'@'+prog.prog_type+'sem'+str(self.semester)+'@'+str(self.year))

class Program_revision(models.Model):  #1.1.2, 1.2.2
    program= models.ForeignKey(Program,on_delete=models.CASCADE)
    revision_year= models.IntegerField(null=True, blank=True)
    percent_of_cont_modified= models.IntegerField(null=True,blank=True)
    document_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return ('revision@'+ str(self.program))


class Mou(models.Model): #3.7.2
    other_party_name=models.CharField(max_length=50,null=True,blank=True)
    institute_name= models.CharField(max_length=50,null=True,blank=True)
    year_of_signing= models.IntegerField(null=True,blank=True)
    duration= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return (self.other_party_name+'@'+self.institute_name)

class Mou_activity(models.Model):  #3.7.2
    mou= models.ForeignKey(Mou,on_delete=models.CASCADE)
    year= models.IntegerField(null=True,blank=True)
    activity_title= models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return (str(self.mou)+'@'+self.activity_title)

class Workshop_seminar(models.Model):   #3.3.2
    name_of_workshop_seminar= models.CharField(max_length=50,null=True,blank=True)
    year_of_conduction= models.IntegerField(null=True,blank=True)
    no_of_participants= models.IntegerField(null=True,blank=True)
    start_date= models.DateField(null=True,blank=True)
    end_date= models.DateField(null=True,blank=True)
    activity_report_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.name_of_workshop_seminar

class Hei_guidence_activity(models.Model):  #5.1.4
    activity_name= models.CharField(max_length=50,null=True,blank=True)
    year_of_conduction= models.IntegerField(null=True,blank=True)
    number_of_students_enrolled= models.IntegerField(null=True,blank=True)
    number_of_students_placed= models.IntegerField(null=True,blank=True)
    document_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.activity_name

class Sports_cultural_event_by_intitution(models.Model):    #5.3.3
    event_name=  models.CharField(max_length=50,null=True,blank=True)
    event_date= models.DateField(null=True,blank=True)
    def __str__(self):
        return self.event_name

class E_governance(models.Model):   #6.2.3
    type=  models.CharField(max_length=50,null=True,blank=True)
    implementation_year= models.IntegerField(null=True,blank=True)
    doc_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.type+'@'+self.str(self.implementation_year)

class Extension_activity_award(models.Model):  #3.6.2
    activity_name= models.CharField(max_length=50,null=True,blank=True)
    award_name= models.CharField(max_length=50,null=True,blank=True)
    awarding_agency_name= models.CharField(max_length=50,null=True,blank=True)
    year_of_awarding= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.activity_name

class Funds_grants_to_inst(models.Model):   #6.4.2
    ngo_name= models.CharField(max_length=50,null=True,blank=True)
    grant_purpose= models.CharField(max_length=50,null=True,blank=True)
    year=  models.IntegerField(null=True,blank=True)
    fund_amount=  models.IntegerField(null=True,blank=True)
    audit_doc_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.ngo_name

class E_library_resource(models.Model): #4.2.2, 4.2.3
    type= models.CharField(max_length=25,null=True,blank=True)
    subscription_details= models.CharField(max_length=100,null=True,blank=True)
    subscription_expenditure= models.IntegerField(null=True,blank=True)
    total_library_expenditure= models.IntegerField(null=True, blank=True)
    year= models.IntegerField(null=True,blank=True)
    doc_link= models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.type

class Prof_dev_skill_enhan_ext_outrch_prog(models.Model):  #6.3.3, 5.1.3, 3.6.3, 3.6.4,
    program_title= models.CharField(max_length=50,null=True,blank=True)
    start_date= models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    no_of_participants= models.IntegerField(null=True,blank=True)
    type= models.CharField(max_length=50,null=True,blank=True)
    agency_or_organizing_unit= models.CharField(max_length=50,null=True,blank=True)
    outrch_prog_scheme_name= models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return (self.program_title+'@'+self.type)










