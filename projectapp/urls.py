from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('coursepage',views.coursepage,name='coursepage'),
    path('studentpage',views.studentpage,name='studentpage'),
    path('th_page',views.th_page,name='th_page'),
    path('showstudentr',views.showstudent,name='showstudent'),
    path('th_table',views.th_table,name='th_table'),
    path('updatestudent/<int:pk>',views.updatestudent,name='updatestudent'),
    path('updateteacher',views.updateteacher,name='updateteacher'),
    path('welcometeacher',views.welcometeacher,name='welcometeacher'),
    path('admin_log',views.admin_log,name='admin_log'),
    path('logout',views.logout,name='logout'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('deletet/<int:pk>',views.deletet,name='deletet'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('edit_teacher/<int:pk>',views.edit_teacher,name='edit_teacher'),
    path('card',views.card,name='card'),
    path('goback',views.goback,name='goback'),
]