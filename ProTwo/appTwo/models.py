from django.db import models

# Create your models here.
MY_CHOICES = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
    )

BRANCH =  (
        ('ETC', 'ETC'),
        ('EEE', 'EEE'),
        ('EE', 'EE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
        ('IT', 'IT'),
        ('CSE', 'CSE'),

    )

CHOICES=(
    ('NO','NO'),
    ('YES','YES'),

    )

CHOICES1=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),

        )

class tech_team(models.Model):
    first_name = models.CharField(max_length = 256,verbose_name = 'Full Name')
    contact = models.IntegerField(verbose_name = 'Contact no.:')
    email = models.EmailField(max_length = 264,unique = True,verbose_name = 'Email Id.:')
    semester = models.CharField(max_length=1, choices=MY_CHOICES,verbose_name = 'Semester')
    branch = models.CharField(max_length=5, choices=BRANCH,verbose_name = 'Branch')
    skills = models.CharField(max_length = 10000,verbose_name = 'What you Know?:',help_text = '(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)')
    interest = models.CharField(max_length = 10000,verbose_name = 'What are you interested in?:',help_text = '(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)')
    workshop = models.CharField(max_length = 10000,verbose_name = 'Attended any workshop?:',help_text = '(e.g.Android development,Drone making,Robotics....etc..)')
    link = models.CharField(max_length = 10000,verbose_name = 'What Projects done till now?:',help_text = '(also give link if uploaded on social sites)')
    paid = models.CharField(max_length=5, choices=CHOICES,verbose_name = 'PAID',default='NO')
    def __str__(self):
        return self.first_name
class Post(models.Model):
    title     =     models.CharField(max_length=100)
    content   =     models.TextField()
    image     =     models.ImageField(upload_to='post_images',blank=True,null=True)
    author    =     models.CharField(max_length=100)
    likes     =     models.IntegerField(blank=True,null=True,default=0)
    image_url =     models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.title
class org_team(models.Model):
    first_name = models.CharField(max_length = 256,verbose_name = 'Full Name')
    contact = models.IntegerField(verbose_name = 'Contact no.:')
    email = models.EmailField(max_length = 264,unique = True,verbose_name = 'Email Id.:')
    semester = models.CharField(max_length=1, choices=MY_CHOICES,verbose_name = 'Semester')
    branch = models.CharField(max_length=5, choices=BRANCH,verbose_name = 'Branch')
    skills = models.CharField(max_length = 10000,verbose_name = 'What you Know?:',help_text = '(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)')
    interest = models.CharField(max_length = 10000,verbose_name = 'What are you interested in?:',help_text = '(e.g. Python,Java,PCB designing,Circuiting,Android Development....etc....)')
    workshop = models.CharField(max_length = 10000,verbose_name = 'Attended any workshop?:',help_text = '(e.g.Android development,Drone making,Robotics....etc..)')
    link = models.CharField(max_length = 10000,verbose_name = 'What Projects done till now?:',help_text = '(also give link if uploaded on social sites)')
    paid = models.CharField(max_length=5, choices=CHOICES,verbose_name = 'PAID',default='NO')
    def __str__(self):
        return self.first_name
class notice_tech(models.Model):
    club_notice_tech = models.TextField(max_length = 10000,verbose_name = 'Area to write latest notice for trchnical teams:',blank=False)
class notice_org(models.Model):
    club_notice_org = models.TextField(max_length = 10000,verbose_name = 'Area to write latest notice for organising teams:',blank=False)




class final_result(models.Model):
    Candidate_name = models.CharField(max_length=100000,verbose_name='Name',blank = True)
    Email_id = models.EmailField(max_length=100000,verbose_name='Email',blank = True)
    Branch = models.CharField(max_length=100000,verbose_name='Branch',blank = True)
    Semester = models.CharField(max_length=100000,verbose_name='Sememster',blank = True)
    Marks_obtained = models.IntegerField(default=0)
    def __str__(self):
        return self.Candidate_name




class Sudent_choice(models.Model):
    User_detail = models.CharField(max_length=100,verbose_name = 'Candidate Name:',default='Your name')
    email = models.EmailField(max_length = 264,unique = True,verbose_name = 'Email Id.:',default='Your Email')
    branch = models.CharField(max_length=5, choices=BRANCH,verbose_name = 'Branch')
    semester = models.CharField(max_length=1, choices=MY_CHOICES,verbose_name = 'Semester')
    question1 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question1',blank = True)
    question2 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question2',blank = True)
    question3 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question3',blank = True)
    question4 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question4',blank = True)
    question5 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question5',blank = True)
    question6 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question6',blank = True)
    question7 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question7',blank = True)
    question8 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question8',blank = True)
    question9 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question9',blank = True)
    question10 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question10',blank = True)
    question11 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question11',blank = True)
    question12 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question12',blank = True)
    question13 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question13',blank = True)
    question14 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question14',blank = True)
    question15 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question15',blank = True)
    #question16 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question16',blank = True)
    #question17 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question17',blank = True)
    #question18 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question18',blank = True)
    #question19 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question19',blank = True)
    #question20 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question20',blank = True)
    #question21 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question21',blank = True)
    #question22 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question22',blank = True)
    #question23 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question23',blank = True)
    #question24 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question24',blank = True)
    #question25 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question25',blank = True)
    #question26 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question26',blank = True)
    #question27 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question27',blank = True)
    #question28 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question28',blank = True)
    #question29 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question29',blank = True)
    #question30 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'question30',blank = True)

    def __str__(self):
        return self.User_detail



class Staff(models.Model):
    question1 = models.TextField(max_length = 100000,verbose_name = 'Question1:' ,blank = True)
    option11 = models.TextField(max_length = 100000,verbose_name = 'Option1.1:' ,blank = True)
    option12 = models.TextField(max_length = 100000,verbose_name = 'Option1.2:' ,blank = True)
    option13 = models.TextField(max_length = 100000,verbose_name = 'Option1.3:' ,blank = True)
    option14 = models.TextField(max_length = 100000,verbose_name = 'Option1.4:' ,blank = True)
    right_option1 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option1',blank = True)


    question2 = models.TextField(max_length = 100000,verbose_name = 'Question2:' ,blank = True)
    option21 = models.TextField(max_length = 100000,verbose_name = 'Option2.1:' ,blank = True)
    option22 = models.TextField(max_length = 100000,verbose_name = 'Option2.2:' ,blank = True)
    option23 = models.TextField(max_length = 100000,verbose_name = 'Option2.3:' ,blank = True)
    option24 = models.TextField(max_length = 100000,verbose_name = 'Option2.4:' ,blank = True)
    right_option2 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option2',blank = True)


    question3 = models.TextField(max_length = 100000,verbose_name = 'Question3:' ,blank = True)
    option31 = models.TextField(max_length = 100000,verbose_name = 'Option3.1:' ,blank = True)
    option32 = models.TextField(max_length = 100000,verbose_name = 'Option3.2:' ,blank = True)
    option33 = models.TextField(max_length = 100000,verbose_name = 'Option3.3:' ,blank = True)
    option34 = models.TextField(max_length = 100000,verbose_name = 'Option3.4:' ,blank = True)
    right_option3 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option3',blank = True)


    question4 = models.TextField(max_length = 100000,verbose_name = 'Question4:' ,blank = True)
    option41 = models.TextField(max_length = 100000,verbose_name = 'Option4.1:' ,blank = True)
    option42 = models.TextField(max_length = 100000,verbose_name = 'Option4.2:' ,blank = True)
    option43 = models.TextField(max_length = 100000,verbose_name = 'Option4.3:' ,blank = True)
    option44 = models.TextField(max_length = 100000,verbose_name = 'Option4.4:' ,blank = True)
    right_option4 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option4',blank = True)


    question5 = models.TextField(max_length = 100000,verbose_name = 'Question5:' ,blank = True)
    option51 = models.TextField(max_length = 100000,verbose_name = 'Option5.1:' ,blank = True)
    option52 = models.TextField(max_length = 100000,verbose_name = 'Option5.2:' ,blank = True)
    option53 = models.TextField(max_length = 100000,verbose_name = 'Option5.3:' ,blank = True)
    option54 = models.TextField(max_length = 100000,verbose_name = 'Option5.4:' ,blank = True)
    right_option5 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option5',blank = True)


    question6 = models.TextField(max_length = 100000,verbose_name = 'Question6:' ,blank = True)
    option61 = models.TextField(max_length = 100000,verbose_name = 'Option6.1:' ,blank = True)
    option62 = models.TextField(max_length = 100000,verbose_name = 'Option6.2:' ,blank = True)
    option63 = models.TextField(max_length = 100000,verbose_name = 'Option6.3:' ,blank = True)
    option64 = models.TextField(max_length = 100000,verbose_name = 'Option6.4:' ,blank = True)
    right_option6 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option6',blank = True)


    question7 = models.TextField(max_length = 100000,verbose_name = 'Question7:' ,blank = True)
    option71 = models.TextField(max_length = 100000,verbose_name = 'Option7.1:' ,blank = True)
    option72 = models.TextField(max_length = 100000,verbose_name = 'Option7.2:' ,blank = True)
    option73 = models.TextField(max_length = 100000,verbose_name = 'Option7.3:' ,blank = True)
    option74 = models.TextField(max_length = 100000,verbose_name = 'Option7.4:' ,blank = True)
    right_option7 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option7',blank = True)


    question8 = models.TextField(max_length = 100000,verbose_name = 'Question8:' ,blank = True)
    option81 = models.TextField(max_length = 100000,verbose_name = 'Option8.1:' ,blank = True)
    option82 = models.TextField(max_length = 100000,verbose_name = 'Option8.2:' ,blank = True)
    option83 = models.TextField(max_length = 100000,verbose_name = 'Option8.3:' ,blank = True)
    option84 = models.TextField(max_length = 100000,verbose_name = 'Option8.4:' ,blank = True)
    right_option8 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option8',blank = True)



    question9 = models.TextField(max_length = 100000,verbose_name = 'Question9:' ,blank = True)
    option91 = models.TextField(max_length = 100000,verbose_name = 'Option9.1:' ,blank = True)
    option92 = models.TextField(max_length = 100000,verbose_name = 'Option9.2:' ,blank = True)
    option93 = models.TextField(max_length = 100000,verbose_name = 'Option9.3:' ,blank = True)
    option94 = models.TextField(max_length = 100000,verbose_name = 'Option9.4:' ,blank = True)
    right_option9 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option9',blank = True)



    question10 = models.TextField(max_length = 100000,verbose_name = 'Question10:' ,blank = True)
    option101 = models.TextField(max_length = 100000,verbose_name = 'Option10.1:' ,blank = True)
    option102 = models.TextField(max_length = 100000,verbose_name = 'Option10.2:' ,blank = True)
    option103 = models.TextField(max_length = 100000,verbose_name = 'Option10.3:' ,blank = True)
    option104 = models.TextField(max_length = 100000,verbose_name = 'Option10.4:' ,blank = True)
    right_option10 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option10',blank = True)



    question11 = models.TextField(max_length = 100000,verbose_name = 'Question11:' ,blank = True)
    option111 = models.TextField(max_length = 100000,verbose_name = 'Option11.1:' ,blank = True)
    option112 = models.TextField(max_length = 100000,verbose_name = 'Option11.2:' ,blank = True)
    option113 = models.TextField(max_length = 100000,verbose_name = 'Option11.3:' ,blank = True)
    option114 = models.TextField(max_length = 100000,verbose_name = 'Option11.4:' ,blank = True)
    right_option11 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option11',blank = True)



    question12 = models.TextField(max_length = 100000,verbose_name = 'Question12:' ,blank = True)
    option121 = models.TextField(max_length = 100000,verbose_name = 'Option12.1:' ,blank = True)
    option122 = models.TextField(max_length = 100000,verbose_name = 'Option12.2:' ,blank = True)
    option123 = models.TextField(max_length = 100000,verbose_name = 'Option12.3:' ,blank = True)
    option124 = models.TextField(max_length = 100000,verbose_name = 'Option12.4:' ,blank = True)
    right_option12 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option12',blank = True)


    question13 = models.TextField(max_length = 100000,verbose_name = 'Question13:' ,blank = True)
    option131 = models.TextField(max_length = 100000,verbose_name = 'Option13.1:' ,blank = True)
    option132 = models.TextField(max_length = 100000,verbose_name = 'Option13.2:' ,blank = True)
    option133 = models.TextField(max_length = 100000,verbose_name = 'Option13.3:' ,blank = True)
    option134 = models.TextField(max_length = 100000,verbose_name = 'Option13.4:' ,blank = True)
    right_option13 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option13',blank = True)


    question14 = models.TextField(max_length = 100000,verbose_name = 'Question14:' ,blank = True)
    option141 = models.TextField(max_length = 100000,verbose_name = 'Option14.1:' ,blank = True)
    option142 = models.TextField(max_length = 100000,verbose_name = 'Option14.2:' ,blank = True)
    option143 = models.TextField(max_length = 100000,verbose_name = 'Option14.3:' ,blank = True)
    option144 = models.TextField(max_length = 100000,verbose_name = 'Option14.4:' ,blank = True)
    right_option14 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option14',blank = True)



    question15 = models.TextField(max_length = 100000,verbose_name = 'Question15:' ,blank = True)
    option151 = models.TextField(max_length = 100000,verbose_name = 'Option15.1:' ,blank = True)
    option152 = models.TextField(max_length = 100000,verbose_name = 'Option15.2:' ,blank = True)
    option153 = models.TextField(max_length = 100000,verbose_name = 'Option15.3:' ,blank = True)
    option154 = models.TextField(max_length = 100000,verbose_name = 'Option15.4:' ,blank = True)
    right_option15 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option15',blank = True)


    question16 = models.TextField(max_length = 100000,verbose_name = 'Question16:' ,blank = True)
    option161 = models.TextField(max_length = 100000,verbose_name = 'Option16.1:' ,blank = True)
    option162 = models.TextField(max_length = 100000,verbose_name = 'Option16.2:' ,blank = True)
    option163 = models.TextField(max_length = 100000,verbose_name = 'Option16.3:' ,blank = True)
    option164 = models.TextField(max_length = 100000,verbose_name = 'Option16.4:' ,blank = True)
    right_option16 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option16',blank = True)



    question17 = models.TextField(max_length = 100000,verbose_name = 'Question17:' ,blank = True)
    option171 = models.TextField(max_length = 100000,verbose_name = 'Option17.1:' ,blank = True)
    option172 = models.TextField(max_length = 100000,verbose_name = 'Option17.2:' ,blank = True)
    option173 = models.TextField(max_length = 100000,verbose_name = 'Option17.3:' ,blank = True)
    option174 = models.TextField(max_length = 100000,verbose_name = 'Option17.4:' ,blank = True)
    right_option17 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option17',blank = True)




    question18 = models.TextField(max_length = 100000,verbose_name = 'Question18:' ,blank = True)
    option181 = models.TextField(max_length = 100000,verbose_name = 'Option18.1:' ,blank = True)
    option182 = models.TextField(max_length = 100000,verbose_name = 'Option18.2:' ,blank = True)
    option183 = models.TextField(max_length = 100000,verbose_name = 'Option18.3:' ,blank = True)
    option184 = models.TextField(max_length = 100000,verbose_name = 'Option18.4:' ,blank = True)
    right_option18 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option18',blank = True)



    question19 = models.TextField(max_length = 100000,verbose_name = 'Question19:' ,blank = True)
    option191 = models.TextField(max_length = 100000,verbose_name = 'Option19.1:' ,blank = True)
    option192 = models.TextField(max_length = 100000,verbose_name = 'Option19.2:' ,blank = True)
    option193 = models.TextField(max_length = 100000,verbose_name = 'Option19.3:' ,blank = True)
    option194 = models.TextField(max_length = 100000,verbose_name = 'Option19.4:' ,blank = True)
    right_option19 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option19',blank = True)



    question20 = models.TextField(max_length = 100000,verbose_name = 'Question20:' ,blank = True)
    option201 = models.TextField(max_length = 100000,verbose_name = 'Option20.1:' ,blank = True)
    option202 = models.TextField(max_length = 100000,verbose_name = 'Option20.2:' ,blank = True)
    option203 = models.TextField(max_length = 100000,verbose_name = 'Option20.3:' ,blank = True)
    option204 = models.TextField(max_length = 100000,verbose_name = 'Option20.4:' ,blank = True)
    right_option20 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option20',blank = True)



    question21 = models.TextField(max_length = 100000,verbose_name = 'Question21:' ,blank = True)
    option211 = models.TextField(max_length = 100000,verbose_name = 'Option21.1:' ,blank = True)
    option212 = models.TextField(max_length = 100000,verbose_name = 'Option21.2:' ,blank = True)
    option213 = models.TextField(max_length = 100000,verbose_name = 'Option21.3:' ,blank = True)
    option214 = models.TextField(max_length = 100000,verbose_name = 'Option21.4:' ,blank = True)
    right_option21 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option21',blank = True)



    question22 = models.TextField(max_length = 100000,verbose_name = 'Question22:' ,blank = True)
    option221 = models.TextField(max_length = 100000,verbose_name = 'Option22.1:' ,blank = True)
    option222 = models.TextField(max_length = 100000,verbose_name = 'Option22.2:' ,blank = True)
    option223 = models.TextField(max_length = 100000,verbose_name = 'Option22.3:' ,blank = True)
    option224 = models.TextField(max_length = 100000,verbose_name = 'Option22.4:' ,blank = True)
    right_option22 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option22',blank = True)



    question23 = models.TextField(max_length = 100000,verbose_name = 'Question23:' ,blank = True)
    option231 = models.TextField(max_length = 100000,verbose_name = 'Option23.1:' ,blank = True)
    option232 = models.TextField(max_length = 100000,verbose_name = 'Option23.2:' ,blank = True)
    option233 = models.TextField(max_length = 100000,verbose_name = 'Option23.3:' ,blank = True)
    option234 = models.TextField(max_length = 100000,verbose_name = 'Option23.4:' ,blank = True)
    right_option23 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option23',blank = True)



    question24 = models.TextField(max_length = 100000,verbose_name = 'Question24:' ,blank = True)
    option241 = models.TextField(max_length = 100000,verbose_name = 'Option24.1:' ,blank = True)
    option242 = models.TextField(max_length = 100000,verbose_name = 'Option24.2:' ,blank = True)
    option243 = models.TextField(max_length = 100000,verbose_name = 'Option24.3:' ,blank = True)
    option244 = models.TextField(max_length = 100000,verbose_name = 'Option24.4:' ,blank = True)
    right_option24 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option24',blank = True)



    question25 = models.TextField(max_length = 100000,verbose_name = 'Question25:' ,blank = True)
    option251 = models.TextField(max_length = 100000,verbose_name = 'Option25.1:' ,blank = True)
    option252 = models.TextField(max_length = 100000,verbose_name = 'Option25.2:' ,blank = True)
    option253 = models.TextField(max_length = 100000,verbose_name = 'Option25.3:' ,blank = True)
    option254 = models.TextField(max_length = 100000,verbose_name = 'Option25.4:' ,blank = True)
    right_option25 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option25',blank = True)



    question26 = models.TextField(max_length = 100000,verbose_name = 'Question26:' ,blank = True)
    option261 = models.TextField(max_length = 100000,verbose_name = 'Option26.1:' ,blank = True)
    option262 = models.TextField(max_length = 100000,verbose_name = 'Option26.2:' ,blank = True)
    option263 = models.TextField(max_length = 100000,verbose_name = 'Option26.3:' ,blank = True)
    option264 = models.TextField(max_length = 100000,verbose_name = 'Option26.4:' ,blank = True)
    right_option26 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option26',blank = True)


    question27 = models.TextField(max_length = 100000,verbose_name = 'Question27:' ,blank = True)
    option271 = models.TextField(max_length = 100000,verbose_name = 'Option27.1:' ,blank = True)
    option272 = models.TextField(max_length = 100000,verbose_name = 'Option27.2:' ,blank = True)
    option273 = models.TextField(max_length = 100000,verbose_name = 'Option27.3:' ,blank = True)
    option274 = models.TextField(max_length = 100000,verbose_name = 'Option27.4:' ,blank = True)
    right_option27 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option27',blank = True)


    question28 = models.TextField(max_length = 100000,verbose_name = 'Question28:' ,blank = True)
    option281 = models.TextField(max_length = 100000,verbose_name = 'Option28.1:' ,blank = True)
    option282 = models.TextField(max_length = 100000,verbose_name = 'Option28.2:' ,blank = True)
    option283 = models.TextField(max_length = 100000,verbose_name = 'Option28.3:' ,blank = True)
    option284 = models.TextField(max_length = 100000,verbose_name = 'Option28.4:' ,blank = True)
    right_option28 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option28',blank = True)


    question29 = models.TextField(max_length = 100000,verbose_name = 'Question29:' ,blank = True)
    option291 = models.TextField(max_length = 100000,verbose_name = 'Option29.1:' ,blank = True)
    option292 = models.TextField(max_length = 100000,verbose_name = 'Option29.2:' ,blank = True)
    option293 = models.TextField(max_length = 100000,verbose_name = 'Option29.3:' ,blank = True)
    option294 = models.TextField(max_length = 100000,verbose_name = 'Option29.4:' ,blank = True)
    right_option29 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option29',blank = True)


    question30 = models.TextField(max_length = 100000,verbose_name = 'Question30:' ,blank = True)
    option301 = models.TextField(max_length = 100000,verbose_name = 'Option30.1:' ,blank = True)
    option302 = models.TextField(max_length = 100000,verbose_name = 'Option30.2:' ,blank = True)
    option303 = models.TextField(max_length = 100000,verbose_name = 'Option30.3:' ,blank = True)
    option304 = models.TextField(max_length = 100000,verbose_name = 'Option30.4:' ,blank = True)
    right_option30 = models.CharField(max_length=5, choices=CHOICES1,verbose_name = 'Right Option30',blank = True)




