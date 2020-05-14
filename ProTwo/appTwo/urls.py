from django.conf.urls import url
from appTwo import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about, name='about'),
    path('bypass/',views.bypass, name='bypass'),
    path('selected_users/',views.selected_users, name='selected_users'),
    path('selected_users_new/',views.selected_users_new, name='selected_users_new'),
    path('work/',views.work, name='work'),
    path('form/',views.tech_teams, name='users'),
    path('form_new/',views.org_teams, name='users_new'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    path('staff_qform/',views.staff_qform, name='staff_qform'),
    path('studentForm/',views.studentForm, name='studentForm'),
    path('aJklkUGgjkF92058HJHNvjrcjg67DGHkjohg/',views.staffpannel_tech, name='staffpannel_tech'),
    path('jkallLLlklklLKL6789305632FFbjsjdcjhk/',views.staffpannel_org, name='staffpannel_org'),
    path('jshgdjhLIILJILJJ09054stploiilFJKOIg/',views.tech_notice_form, name='tech_notice_form'),
    path('lortyuioJKJGFD53298FJJH586ardgklseo/',views.org_notice_form, name='org_notice_form'),
    path('completed_projects/',views.completed_projects, name='completed_projects'),
]
