from django.http import JsonResponse
from django.shortcuts import render ,redirect
from .forms import UserReg
from .models import UserModel
import json
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# from django.views.decorators.csrf import csrf_exempt
# Create your views he
def home(request):
    form=UserReg
    std=UserModel.objects.all()
    return render(request,'home.html',{'form':form,'stu':std})
# @csrf_exempt
def save(request):
    if request.method=='POST':
        form=UserReg(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            name=request.POST['name']
            number=request.POST['number']
            adress=request.POST['adress']
            if sid=="":
                usr=UserModel(name=name,number=number,adress=adress,)
            else:
                usr=UserModel(id=sid,name=name,number=number,adress=adress,)
            usr.save()
            info=UserModel.objects.values()
            stud_data=list(info)
            return JsonResponse({"status":"save","stud_data":stud_data})
        else:
            return JsonResponse({"status":"error"})

def delete(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        pi=UserModel.objects.get(pk=id)
        pi.delete()
        return JsonResponse({"status":"done"})
    else:
        return JsonResponse({"status":"error"})


def edit(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        student=UserModel.objects.get(pk=id)
        student_data={"id":student.id,"name":student.name,"number":student.number,"adress":student.adress}
        return JsonResponse(student_data)

def search(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get("searchText")
        
        searching=UserModel.objects.filter(
            name__icontains=search_str) or UserModel.objects.filter(
            number__icontains=search_str) or UserModel.objects.filter(
            adress__icontains=search_str)
        data=searching.values()
        return JsonResponse(list(data),safe=False)  


def Login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or password is incorrect ")
            return redirect('login')
    
    return render(request,'login.html')

def RegForm(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('login')
    context={"form":form}
    return render(request,'register.html',context)



class ProfileView(TemplateView):
    template_name="profile.html"

def logoutuser(request):
    logout(request)
    messages.info(request,"you have been logged Out")
    return redirect("/")