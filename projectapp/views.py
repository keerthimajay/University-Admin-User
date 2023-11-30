from django.shortcuts import render,redirect
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from .models import Courses,StudentDetails,TeacherDetails


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def dashboard(request):
    return render(request,'dashboard.html')

def coursepage(request):
    return render(request,'coursepage.html')

def studentpage(request):
    a = Courses.objects.all()
    return render(request,'studentpage.html',{'course':a})

def showstudent(request):
    b=StudentDetails.objects.all()
    return render(request,'showstudent.html',{'sho':b})

def th_table(request):   
    k=TeacherDetails.objects.all()
    return render(request,'th_table.html',{'thr':k})

def updatestudent(request,pk):
    c=StudentDetails.objects.get(id=pk)
    d=Courses.objects.all()
    return render(request,'updatestudent.html',{'std':c,'cou':d})

def th_page(request):
    e= Courses.objects.all()
    return render(request,'th_page.html',{'pr':e})

def updateteacher(request):
    p=TeacherDetails.objects.get(user=request.user)
    v=Courses.objects.all()
    return render(request,'updateteacher.html',{'tec':p,'co':v})



def welcometeacher(request):
    return render(request,'welcometeacher.html')


def card(request):
    n=TeacherDetails.objects.get(user=request.user)
    m=Courses.objects.all()
    return render(request,'card.html',{'tr':n,'cr':m})

def admin_log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('dashboard')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('welcometeacher')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    return render(request,'th_page.html')


def logout(request):
    return render(request,'homepage.html')

def add_course(request):
    if request.method=='POST':
        cname = request.POST['course']
        fee = request.POST['fees']
        x = Courses(course_name=cname,fee=fee)
        x.save()
        return redirect('studentpage')

 
def add_student(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        age = request.POST['age']
        doj = request.POST['doj']
        qual = request.POST['qualification']
        y = Courses.objects.get(id=qual)
        z = StudentDetails(student_fname=fname,student_lname=lname,address=address,age=age,doj=doj,course=y)
        z.save()
        return redirect('showstudent')
  
def edit_student(request,pk):
    if request.method=='POST':
        student = StudentDetails.objects.get(id=pk)
        student.student_fname=request.POST.get('fname')
        student.student_lname=request.POST.get('lname')
        student.address=request.POST.get('address')
        student.age=request.POST.get('age')
        student.doj=request.POST.get('doj')
        e=request.POST['qualification']
        f=request.POST['fees']
        g=Courses.objects.get(id=e)
        g.fee=f
        g.save()
        student.course=g
        student.save()
        return redirect('showstudent')
    return render(request,'updatestudent.html')


def delete(request,pk):
        std=StudentDetails.objects.get(id=pk)
        std.delete()
        return redirect('showstudent')


 
def deletet(request,pk):
        cour=User.objects.get(id=pk)
        tcrh=TeacherDetails.objects.get(user=pk)
        tcrh.delete()
        cour.delete()
        return redirect('th_table')
    


def add_teacher(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['username']
        pswd=request.POST['password']
        cpswd=request.POST['cpassword']
        email=request.POST['email']
        addr=request.POST['address']
        age=request.POST['age']
        number=request.POST['phone']
        sel=request.POST['sel']
        doj=request.POST['doj']
        image=request.FILES.get('image')
        if pswd==cpswd: 
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('homepage')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pswd,
                    email=email)
                user.save()
                course2=Courses.objects.get(id=sel)
                u=User.objects.get(id=user.id)
                reg=TeacherDetails(address=addr,age=age,doj=doj,phone=number,course=course2,img=image,user=u)
                reg.save()
                return redirect('homepage')
        else:
            messages.info(request,'password incorrect')
            return redirect('/')




def edit_teacher(request,pk):
    if request.method=='POST':
        teacher = TeacherDetails.objects.get(user=pk)
        user = User.objects.get(id=pk)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['username']
        user.email=request.POST['email']
        teacher.age=request.POST.get('age')
        teacher.phone=request.POST.get('phone')
        teacher.address=request.POST.get('address')
        teacher.doj=request.POST.get('doj')
        #teacher.img=request.FILES.get('image')
        courseid=request.POST['sel']
        course=Courses.objects.get(id=courseid)
        teacher.course=course
        newimg=request.FILES.get('image')
        if newimg:
            if teacher.img:
                os.remove(teacher.img.path)
                teacher.img=newimg
        teacher.save()
        user.save()
        return redirect('card')
   


def goback(request):
    return redirect('welcometeacher')