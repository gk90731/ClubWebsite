from django.shortcuts import render
from appTwo.models import User

from appTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def about(request):
    return render(request,'appTwo/about.html')

def work(request):
    return render(request,'appTwo/work.html')

def completed_projects(request):
    return render(request,'appTwo/completed_projects.html')




def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'appTwo/member.html',{'form':form})


def selected_users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'appTwo/team.html',context=user_dict)
