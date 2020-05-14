"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from appTwo import views
urlpatterns = [
    path('',views.index, name='home'),
    path('team/',views.team, name='team'),
    path('about/',views.about, name='about'),
    path('campus/',views.campus, name='campus'),
    path('selected_users/',views.selected_users, name='selected_users'),
    path('selected_users_new/',views.selected_users_new, name='selected_users_new'),
    path('bypass/',views.bypass, name='bypass'),
    path('staff_qform/',views.staff_qform, name='staff_qform'),
    path('studentForm/',views.studentForm, name='studentForm'),
    path('work/',views.work, name='work'),
    path('form/',views.tech_teams, name='users'),
    path('form_new/',views.org_teams, name='users_new'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    path('aJklkUGgjkF92058HJHNvjrcjg67DGHkjohg/',views.staffpannel_tech, name='staffpannel_tech'),
    path('jkallLLlklklLKL6789305632FFbjsjdcjhk/',views.staffpannel_org, name='staffpannel_org'),
    path('jshgdjhLIILJILJJ09054stploiilFJKOIg/',views.tech_notice_form, name='tech_notice_form'),
    path('lortyuioJKJGFD53298FJJH586ardgklseo/',views.org_notice_form, name='org_notice_form'),
    path('lortyuioJKJlogjio8905dfgH586ardgklseo/',views.createBlog, name='createBlog'),
    path('blogs/',views.createBlogPost, name='blogs'),

    path('completed_projects/',views.completed_projects, name='completed_projects'),
    path('admin/', admin.site.urls)
]
