from django.shortcuts import render
from appTwo.models import tech_team,org_team,Staff,Sudent_choice,final_result,notice_tech,notice_org,Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm,StaffForm,Sudent_choiceForm,Notice_Tech,Notice_Org

from django.template.loader import render_to_string
from appTwo.forms import NewUserForm,NewUserForm_new
from django.template import Context
from django.template.loader import get_template
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
def index(request):

    return render(request,'index.html')
@csrf_exempt
@parser_classes([MultiPartParser])
@api_view(['POST','GET','PUT','OPTIONS'])
def createBlog(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == "PUT":
        if Post.objects.all().filter(id=request.data["postId"]).exists():
            like_obj = Post.objects.get(id = request.data["postId"])
            like_obj.likes = like_obj.likes+1
            like_obj.save()
            return Response({"response":"exists"})
        else:
            return Response({"response":"does not exists"})
    if request.method == "POST":
        try:
            final = Post(title=request.data["title"],content=request.data["content"],image=request.data["image"],author=request.data["author"])
            final.save()
        except:
            final = Post(title=request.data["title"],content=request.data["content"],image="",author=request.data["author"])
            final.save()
    if request.method == "OPTIONS":
        post = Post.objects.all().filter(id=request.data["postId"])
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    return Response({"success":"success"})
def createBlogPost(request):
    return render(request,'createBlog.html')
def about(request):
    return render(request,'about.html')
def campus(request):
    return render(request,'CampusAmb.html')
def team(request):
    return render(request,'team.html')

def bypass(request):
    return render(request,'bypass.html')

def work(request):
    return render(request,'work.html')

def completed_projects(request):
    return render(request,'completed_projects.html')
def staffpannel_tech(request):
    user_list = tech_team.objects.order_by('first_name')
    user_dict = {'tech_team': user_list}
    return render(request,'staffpannel.html',context=user_dict)
def staffpannel_org(request):
    user_list = org_team.objects.order_by('first_name')
    user_dict = {'org_team': user_list}
    return render(request,'staffpannel_org.html',context=user_dict)

def tech_teams(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return registraion_success(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'tech_team_form.html',{'form':form})

def org_teams(request):

    form = NewUserForm_new()

    if request.method == "POST":
        form = NewUserForm_new(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return registraion_success_new(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'org_team_form.html',{'form':form})
def registraion_success(request):
    team_list = tech_team.objects.all().last()
    team = str(team_list.email)
    team1 = team.lower()
    body = (
                str(team_list.first_name)+'\n'+str(team_list.contact)+'\n'+str(team_list.email)+'\n'+str(team_list.semester)+'\n'+str(team_list.branch)+'\n'+str(team_list.skills)+'\n'+str(team_list.interest)+'\n'+str(team_list.workshop)+'\n'+str(team_list.link)+'\n'
                )
    send_mail('TechnoHub Registration','Please submit registraion charge (Rs. 100) by calling on 7722874355 to Sachet Sabrad and get your registration approved.\nFor further queries contact Kumar Gaurav on 7000542882\n\n Regards TechnoHub', 'bit.technohub@gmail.com', [team1])
    send_mail('TechnoHub Registration',body, 'bit.technohub@gmail.com', ['bit.technohub@gmail.com'])

    return HttpResponse('Success! Thankyou for you registration. <br><p><a href = "http://technohubbit.pythonanywhere.com/selected_users/">click here</a> to go to Technical Team page</p>')
def registraion_success_new(request):
    org_list = org_team.objects.all().last()
    org = str(org_list.email)
    org1 = org.lower()
    body = (
            str(org_list.first_name)+'\n'+str(org_list.contact)+'\n'+str(org_list.email)+'\n'+str(org_list.semester)+'\n'+str(org_list.branch)+'\n'+str(org_list.skills)+'\n'+str(org_list.interest)+'\n'+str(org_list.workshop)+'\n'+str(org_list.link)+'\n'
            )
    send_mail('TechnoHub Registration','Please submit registraion charge (Rs. 100) by calling on 7722874355 to Sachet Sabrad and get your registration approved.\nFor further queries contact Kumar Gaurav on 7000542882\n\n Regards TechnoHub', 'bit.technohub@gmail.com', [str(org1)])
    send_mail('TechnoHub Registration',body, 'bit.technohub@gmail.com', ['bit.technohub@gmail.com'])

    return HttpResponse('Success! Thankyou for you registration. <br><p><a href = "http://technohubbit.pythonanywhere.com/selected_users_new/">click here</a> to go to Organising Team page</p>')




def tech_notice_form(request):

    form = Notice_Tech()

    if request.method == "POST":
        form = Notice_Tech(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return notice_tech_view(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'tech_notice.html',{'form':form})
def notice_tech_view(request):
    last_notice_tech = notice_tech.objects.all().last()
    team = str(last_notice_tech.club_notice_tech)
    team1 = team.lower()
    body = (
                str(last_notice_tech.club_notice_tech)+'\n'+'\n Regards TechnoHub'
                )
    tech_email = []
    user_list = tech_team.objects.order_by('first_name')
    for pe in user_list:
        tech_emails = pe.email
        tech_email.append(tech_emails)
    send_mail('TechnoHub Notice',body, 'bit.technohub@gmail.com', tech_email)
    return HttpResponse('<h3>Notice sent sucessfully.Please go back to <a href ="www.technohubbit.in">home</a> </h3>')
def org_notice_form(request):

    form = Notice_Org()

    if request.method == "POST":
        form = Notice_Org(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return notice_Org_view(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'Org_notice.html',{'form':form})
def notice_Org_view(request):
    last_notice_Org = notice_org.objects.all().last()
    team = str(last_notice_Org.club_notice_org)
    team1 = team.lower()
    body = (
                str(last_notice_Org.club_notice_org)+'\n'+'\n Regards TechnoHub'
                )
    Org_email = []
    user_list = org_team.objects.order_by('first_name')
    for pe in user_list:
        Org_emails = pe.email
        Org_email.append(Org_emails)
    send_mail('TechnoHub Notice',body, 'bit.technohub@gmail.com', Org_email)
    return HttpResponse('<h3>Notice sent sucessfully.Please go back to <a href ="www.technohubbit.in">home</a> </h3>')




































def selected_users(request):
    user_list = tech_team.objects.order_by('first_name')
    user_dict = {'tech_teams': user_list}
    return render(request,'tech_members.html',context=user_dict)

def selected_users_new(request):
    user_list = org_team.objects.order_by('first_name')
    user_dict = {'org_teams': user_list}
    return render(request,'org_members.html',context=user_dict)

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(your_email,message,subject,['bit.technohub@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


########################################### staff form for question #################################################
def staff_qform(request):

    form = StaffForm()

    if request.method == "POST":
        form = StaffForm(request.POST)

        form.save(commit = True)

        return index(request)
    else:
        print('ERROR FORM INVALID')

    return render(request,'staffform.html',{'form':form})

########################################## Candidate Result ####################################################################
def candidate_result(request):
    user_list_new_new_new = Sudent_choice.objects.all().last()
    user_list_new_new = Staff.objects.order_by('right_option1')
    uset        =Staff.objects.all().last()

#list admin################################
    list2 = []
    for person in user_list_new_new:

        person_new1 = person.right_option1
        person_new2 = person.right_option2
        person_new3 = person.right_option3
        person_new4 = person.right_option4
        person_new5 = person.right_option5
        person_new6 = person.right_option6
        person_new7 = person.right_option7
        person_new8 = person.right_option8
        person_new9 = person.right_option9
        person_new10 = person.right_option10
        person_new11 = person.right_option11
        person_new12 = person.right_option12
        person_new13 = person.right_option13
        person_new14 = person.right_option14
        person_new15 = person.right_option15

        list2.append(person_new1)
        list2.append(person_new2)
        list2.append(person_new3)
        list2.append(person_new4)
        list2.append(person_new5)
        list2.append(person_new6)
        list2.append(person_new7)
        list2.append(person_new8)
        list2.append(person_new9)
        list2.append(person_new10)
        list2.append(person_new11)
        list2.append(person_new12)
        list2.append(person_new13)
        list2.append(person_new14)
        list2.append(person_new15)

    user_list_newrr = list2
#list user##########################################

    #for person in user_list_new_new_new:
    list1 = []
    person_new1 = user_list_new_new_new.question1
    person_new2 = user_list_new_new_new.question2
    person_new3 = user_list_new_new_new.question3
    person_new4 = user_list_new_new_new.question4
    person_new5 = user_list_new_new_new.question5
    person_new6 = user_list_new_new_new.question6
    person_new7 = user_list_new_new_new.question7
    person_new8 = user_list_new_new_new.question8
    person_new9 = user_list_new_new_new.question9
    person_new10 = user_list_new_new_new.question10
    person_new11 = user_list_new_new_new.question11
    person_new12 = user_list_new_new_new.question12
    person_new13 = user_list_new_new_new.question13
    person_new14 = user_list_new_new_new.question14
    person_new15 = user_list_new_new_new.question15



    list1.append(person_new1)
    list1.append(person_new2)
    list1.append(person_new3)
    list1.append(person_new4)
    list1.append(person_new5)
    list1.append(person_new6)
    list1.append(person_new7)
    list1.append(person_new8)
    list1.append(person_new9)
    list1.append(person_new10)
    list1.append(person_new11)
    list1.append(person_new12)
    list1.append(person_new13)
    list1.append(person_new14)
    list1.append(person_new15)








    user_list_newr = list1
    #gau = user_list_new_new_new



    result1 = 0
    #incorrect = []
    #for w in list2:
    #    result1 += list1.count(w)
    #for x,y in zip(set(list1), list2):
    #    if x != y:
    #        incorrect.append(y)
    #result1 = len(incorrect)
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            result1 += 1

    unattempted = list1.count('')
    virtual_wrong = len(list1) - result1
    wrong = virtual_wrong - unattempted
    marks_obtained = wrong*(-1)+unattempted*(0)+result1*(1)
    student = final_result()
    student.Marks_obtained = marks_obtained
    student.Candidate_name =    user_list_new_new_new.User_detail
    student.Email_id =          user_list_new_new_new.email
    pl = user_list_new_new_new.email
    #student.Branch   =          user_list_new.
    #student.Semester =          user_list_new.
    student.save()
    body = ('your obtained marks:'+' '+str(marks_obtained)+'    '+'\n'
    +'Your selections:'+'\n'
    +'Question 1 :'+'  '+str(user_list_new_new_new.question1)+'\n'
    +'Question 2 :'+'  '+str(user_list_new_new_new.question2)+'\n'
    +'Question 3 :'+'  '+str(user_list_new_new_new.question3)+'\n'
    +'Question 4 :'+'  '+str(user_list_new_new_new.question4)+'\n'
    +'Question 5 :'+'  '+str(user_list_new_new_new.question5)+'\n'
    +'Question 6 :'+'  '+str(user_list_new_new_new.question6)+'\n'
    +'Question 7 :'+'  '+str(user_list_new_new_new.question7)+'\n'
    +'Question 8 :'+'  '+str(user_list_new_new_new.question8)+'\n'
    +'Question 9 :'+'  '+str(user_list_new_new_new.question9)+'\n'
    +'Question 10 :'+'  '+str(user_list_new_new_new.question10)+'\n'
    +'Question 11 :'+'  '+str(user_list_new_new_new.question11)+'\n'
    +'Question 12 :'+'  '+str(user_list_new_new_new.question12)+'\n'
    +'Question 13 :'+'  '+str(user_list_new_new_new.question13)+'\n'
    +'Question 14 :'+'  '+str(user_list_new_new_new.question14)+'\n'
    +'Question 15 :'+'  '+str(user_list_new_new_new.question15)+'\n'

    +str(uset.question1)+'\n'+str(uset.option11)+'\n'+str(uset.option12)+'\n'+str(uset.option13)+'\n'+str(uset.option14)+'\n'+'Right Option:'+'  '+str(uset.right_option1)+'\n'
    +str(uset.question2)+'\n'+str(uset.option21)+'\n'+str(uset.option22)+'\n'+str(uset.option23)+'\n'+str(uset.option24)+'\n'+'Right Option:'+'  '+str(uset.right_option2)+'\n'
    +str(uset.question3)+'\n'+str(uset.option31)+'\n'+str(uset.option32)+'\n'+str(uset.option33)+'\n'+str(uset.option34)+'\n'+'Right Option:'+'  '+str(uset.right_option3)+'\n'
    +str(uset.question4)+'\n'+str(uset.option41)+'\n'+str(uset.option42)+'\n'+str(uset.option43)+'\n'+str(uset.option44)+'\n'+'Right Option:'+'  '+str(uset.right_option4)+'\n'
    +str(uset.question5)+'\n'+str(uset.option51)+'\n'+str(uset.option52)+'\n'+str(uset.option53)+'\n'+str(uset.option54)+'\n'+'Right Option:'+'  '+str(uset.right_option5)+'\n'
    +str(uset.question6)+'\n'+str(uset.option61)+'\n'+str(uset.option62)+'\n'+str(uset.option63)+'\n'+str(uset.option64)+'\n'+'Right Option:'+'  '+str(uset.right_option6)+'\n'
    +str(uset.question7)+'\n'+str(uset.option71)+'\n'+str(uset.option72)+'\n'+str(uset.option73)+'\n'+str(uset.option74)+'\n'+'Right Option:'+'  '+str(uset.right_option7)+'\n'
    +str(uset.question8)+'\n'+str(uset.option81)+'\n'+str(uset.option82)+'\n'+str(uset.option83)+'\n'+str(uset.option84)+'\n'+'Right Option:'+'  '+str(uset.right_option8)+'\n'
    +str(uset.question9)+'\n'+str(uset.option91)+'\n'+str(uset.option92)+'\n'+str(uset.option93)+'\n'+str(uset.option94)+'\n'+'Right Option:'+'  '+str(uset.right_option9)+'\n'
    +str(uset.question10)+'\n'+str(uset.option101)+'\n'+str(uset.option102)+'\n'+str(uset.option103)+'\n'+str(uset.option104)+'\n'+'Right Option:'+'  '+str(uset.right_option10)+'\n'
    +str(uset.question11)+'\n'+str(uset.option111)+'\n'+str(uset.option112)+'\n'+str(uset.option113)+'\n'+str(uset.option114)+'\n'+'Right Option:'+'  '+str(uset.right_option11)+'\n'
    +str(uset.question12)+'\n'+str(uset.option121)+'\n'+str(uset.option122)+'\n'+str(uset.option123)+'\n'+str(uset.option124)+'\n'+'Right Option:'+'  '+str(uset.right_option12)+'\n'
    +str(uset.question13)+'\n'+str(uset.option131)+'\n'+str(uset.option132)+'\n'+str(uset.option133)+'\n'+str(uset.option134)+'\n'+'Right Option:'+'  '+str(uset.right_option13)+'\n'
    +str(uset.question14)+'\n'+str(uset.option141)+'\n'+str(uset.option142)+'\n'+str(uset.option143)+'\n'+str(uset.option144)+'\n'+'Right Option:'+'  '+str(uset.right_option14)+'\n'
    +str(uset.question15)+'\n'+str(uset.option151)+'\n'+str(uset.option152)+'\n'+str(uset.option153)+'\n'+str(uset.option154)+'\n'+'Right Option:'+'  '+str(uset.right_option15)+'\n'

        )
    send_mail('saturday_test_marks_obtained',  body , 'bit.technohub@gmail.com', [str(pl)])
    user_dict = {'staff_qform': user_list_new_new,'candidate_result':user_list_new_new_new,'user_list_newre':result1,'user_list_newrf':unattempted,'user_list_newrg':wrong,'user_list_newrh':marks_obtained,'user_list_newr':user_list_newr,'user_list_newrr':user_list_newrr}
    return render(request,'result.html',context=user_dict)
####################################question paper############################################
def studentForm(request):

    form = Sudent_choiceForm()
    user_list = Staff.objects.order_by('question1')
    user_dict = {'staff_qform': user_list,'form':form}

    if request.method == "POST":
        form = Sudent_choiceForm(request.POST)

        form.save(commit = True)
        #return render(request,'team.html',context=user_dict)
        return candidate_result(request)
    else:
        print('ERROR FORM INVALID')


    return render(request,'aptitude.html',context=user_dict)
