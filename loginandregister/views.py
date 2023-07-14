from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from loginandregister.models import Alluser
# Create your views here.
def displayhomepage(request):
    rend=render(request,'loginandregister/login.html')
    return rend

def validateuser(request):
    if request.method!='POST':
        return HttpResponseRedirect('http://localhost:8000/loginandregister/login/')
    else:
        username= request.POST['username']
        pwd= request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)
            alluser= Alluser.objects.get(pk=user.id)
            if alluser.user_type =='Student':
                return HttpResponseRedirect('/student/home/')
            elif alluser.user_type =='Teacher':
                return HttpResponseRedirect('/teacher/home/')
            elif alluser.user_type == 'Academic':
                return HttpResponseRedirect('/institute/academic_home/')
            elif alluser.user_type== 'Account':
                return HttpResponseRedirect('/institute/account_home/')
            elif alluser.user_type== 'Sport':
                return HttpResponseRedirect('/institute/sport_home/')
            elif alluser.user_type=='Library':
                return HttpResponseRedirect('/institute/library_home/')
            elif alluser.user_type=='NAAC_Cordinator':
                return HttpResponseRedirect('/institute/naac_cod_home/')
            elif alluser.user_type=='Admin':
                return HttpResponseRedirect('/institute/admin_home/')
        else:
            return HttpResponse('Invalid Creds')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('http://localhost:8000/loginandregister/login/')