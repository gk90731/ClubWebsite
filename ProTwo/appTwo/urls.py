from django.conf.urls import url
from appTwo import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about, name='about'),
    path('selected_users/',views.selected_users, name='selected_users'),
    path('work/',views.work, name='work'),
    path('form/',views.users, name='users'),
    path('completed_projects/',views.completed_projects, name='completed_projects'),
]
