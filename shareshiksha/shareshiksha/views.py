from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Admin,Community,CommunitySchoolRel,School,Teacher,Volunteer,Grievance

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, 'index.html')

def admin_login(request,*args, **kwargs):
    return render(request, 'admin_login.html')

def member_login(request,*args, **kwargs):
    return render(request, 'member_login.html')

def contact(request,*args, **kwargs):
    return render(request, 'contact.html')
    

def grievances_form(request):
    return render(request,'grievance.html')

def addgrievance(request):
    new_item = Grievance(name = request.POST['name'], community=request.POST['community'],msg=request.POST['msg'])
    new_item.save()
    return HttpResponseRedirect('../')

def currgrievance(request):
    all_grievances1 = Grievance.objects.all()

    return render(request,'curgrievance.html',
    {'all_grievances' : all_grievances1}
    )

def updateresource(request, *args, **kwargs):
    num = request.POST['num']  #take integer as input here
    str = request.POST['resource']
    if str == "resource1":
        item_A = School(resource1 = request.POST['school1'])
        item_B = School(resource1 = request.POST['school2'])
        item_A.r1 = item_A.r1 + num
        item_B.r1 = item_B.r1 - num
    if str == "resource2":
        item_A = School(resource2 = request.POST['school1'])
        item_B = School(resource2 = request.POST['school2'])
        item_A.r1 = item_A.r1 + num
        item_B.r1 = item_B.r1 - num
    if str == "resource3":
        item_A = School(resource3 = request.POST['school1'])
        item_B = School(resource3 = request.POST['school2'])
        item_A.r1 = item_A.r1 + num
        item_B.r1 = item_B.r1 - num
    item_A.save()
    item_B.save()
    return HttpResponseRedirect('../admin_login/')

def memberpage(request):
    return render(request,'memberpage.html')

def adminpage(request):
    return render(request,'adminpage.html')


    
    
