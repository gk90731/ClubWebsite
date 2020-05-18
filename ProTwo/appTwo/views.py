from django.shortcuts import render
from appTwo.models import tech_team,org_team,notice_tech,notice_org,Post,AptiQuestion,AptiOption,AptiTest,AptiStudent
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm,Notice_Tech,Notice_Org

from django.template.loader import render_to_string
from appTwo.forms import NewUserForm,NewUserForm_new
from django.template import Context
from django.template.loader import get_template
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.exceptions import APIException
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



# Aptitude View Section Start ###################################################################################################

# class AptiOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AptiOption
#         fields = ('option1','option2','option3','option4')
# class AptiQuestionSerializer(serializers.ModelSerializer):
#     option_set = AptiOptionSerializer(read_only=True,many=True)
#     class Meta:
#         model = AptiQuestion
#         fields = ('question', 'option_set',)


class AptiOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AptiOption
        fields = ('id','option1','option2','option3','option4')

class TestInfoSerializer(serializers.ModelSerializer):
    total_question = serializers.SerializerMethodField()
    def get_total_question(self, obj):
        return AptiQuestion.objects.all().filter(test_no=AptiTest.objects.latest('test_number')).count()
    class Meta:
        model = AptiTest
        fields = ('test_number', 'duration', 'total_question')

class AptiQuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    def get_choices(self, obj):
        ordered_queryset = AptiOption.objects.filter(question_no_id=obj.id)
        return AptiOptionSerializer(ordered_queryset, many=True, context=self.context).data
    class Meta:
        model = AptiQuestion
        fields = ('id', 'question', 'choices')




@api_view(['GET','POST','PUT'])
def AptiQuestionView(request):
    if request.method == "GET":
        # get the last test number
        lastest_test_instance = AptiTest.objects.latest('test_number')
        # get all questions and options relation with latest test number
        AptiQuestions = AptiQuestion.objects.all().filter(test_no=lastest_test_instance)
        # pass this all questions and options to serializer to give latest question and option json
        QuestionSerializer = AptiQuestionSerializer(AptiQuestions, many=True)
        TestInfoSerializer_obj = TestInfoSerializer(lastest_test_instance)
        return Response({"TestInfo":TestInfoSerializer_obj.data,"Questions":QuestionSerializer.data})
    if request.method == "POST":
        #  first get the data when post method hit
        if not AptiStudent.objects.filter(email=request.data["email"],test_no=AptiTest.objects.get(test_number=request.data["test_no"])).exists():
            CreateStudentProfile = AptiStudent(full_name=request.data["name"],branch=request.data["branch"], email=request.data["email"], semester=request.data["semester"],contact=request.data["contact_no"],test_no=AptiTest.objects.get(test_number=request.data["test_no"]))
            CreateStudentProfile.save()
            return HttpResponse(status=201)
        return Response({"error":"You already attempetd the test"})
        if request.data == {}:
            raise APIException({"name":"required",
                                "branch":"required",
                                "semester":"required",
                                "contact_no":"required",
                                "email":"required",
                                "test_no":"required",
                                "question_option":[{"option_id":"required","selected_option":"required"},"..."]})
        return HttpResponse(status=400)
    if request.method == "PUT":
        studentSelections = request.data['studentSelections']
        correctOptionList = [i.answer for i in AptiOption.objects.filter(pk__in=[i["id"] for i in studentSelections])] #right option list
        studentSelectionsList = [] #student Selection List
        for i in studentSelections:
            studentSelectionsList.append(i["value"]) 

        correct_answered = 0
        for i in range(len(correctOptionList)):
            if correctOptionList[i] == studentSelectionsList[i]:
                correct_answered += 1

        total_questions = len(correctOptionList)

        unattempted = studentSelectionsList.count('')

        attempted = len(correctOptionList)-unattempted

        wrong_answered = attempted-correct_answered

        marks_obtained = (correct_answered*1)-(wrong_answered*1)

        print("total_questions",total_questions)
        print("marks_obtained",marks_obtained)
        print("wrong_answered",wrong_answered)
        print("unattempted",unattempted)
        print("correct_answered",correct_answered)  
        #  fetch the right option from database with respect to question
        #  algorithm to check for no. of attempted, no. of unattempted, marks obtained
        #  save the student data and marks obtained in database
        #  send the mail including marks obtained and attachment with right option and explanation
        print(request.data['studentDetail']['test_no'],"hey uuhhhhhhh")
        TestObj = AptiTest.objects.get(test_number=request.data['studentDetail']['test_no'])
        StudentObj = AptiStudent.objects.get(email=request.data['studentDetail']['email'],test_no=TestObj)
        StudentObj.marks_obt = marks_obtained
        StudentObj.save()

        from django.core.mail import EmailMultiAlternatives
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags

        subject, from_email, to = 'Your Report Card is Here', 'bit.technohub@gmail.com', request.data['studentDetail']['email']

        html_content = render_to_string('email.html', {"attempted":attempted,"unattempted":unattempted,"wrong_answered":wrong_answered,"marks_obtained":marks_obtained,"total_questions":attempted+unattempted}) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response({"attempted":attempted,"unattempted":unattempted,"wrong_answered":wrong_answered,"marks_obtained":marks_obtained})
    return Response({"error":"some error"})
# Aptitude View Section End #####################################################################################################


def test(request):
    return render(request,'build/aptiBuild/build/index.html')