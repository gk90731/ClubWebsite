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
        ('CS', 'CS'),
        ('MCA', 'MBA'),
        ('MBA', 'MBA')

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



# section for aptitude test start ##############################################################################################

class AptiTest(models.Model):
    test_number         = models.IntegerField(verbose_name = 'Test number', blank=True, unique=True)
    duration            = models.TimeField(auto_now=False, auto_now_add=False,blank=False)
    def __str__(self):
        return "Test"+str(self.test_number)


class AptiQuestion(models.Model):
    test_no             = models.ForeignKey(AptiTest, on_delete=models.CASCADE, verbose_name = 'Test no.:')
    question            = models.TextField(max_length = 10000,verbose_name = 'Write your question here')    
    def __str__(self):
        return str(str(self.test_no)+" : "+self.question)

class AptiOption(models.Model):
    question_no         = models.ForeignKey(AptiQuestion, on_delete=models.CASCADE, verbose_name = 'Question:', unique=True)
    option1             = models.CharField(max_length = 500,verbose_name = 'Option1' ,blank=True)
    option2             = models.CharField(max_length = 500,verbose_name = 'Option2' ,blank=True)
    option3             = models.CharField(max_length = 500,verbose_name = 'Option3' ,blank=True)
    option4             = models.CharField(max_length = 500,verbose_name = 'Option4' ,blank=True)
    choose              = (('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4'))
    answer              = models.CharField(max_length=10, choices=choose, verbose_name = 'Right Answer')
    def __str__(self):
        return str(self.question_no)

class AptiStudent(models.Model):
    full_name           = models.CharField(max_length = 256,verbose_name = 'Full Name')
    email               = models.EmailField(verbose_name = 'Email')
    semester            = models.CharField(max_length=1, choices=MY_CHOICES,verbose_name = 'Semester')
    branch              = models.CharField(max_length=10, choices=BRANCH,verbose_name = 'Branch')
    contact             = models.IntegerField(verbose_name = 'Contact no.:')
    test_no             = models.ForeignKey(AptiTest, on_delete=models.CASCADE, verbose_name = 'Test no.:')
    marks_obt           = models.IntegerField(verbose_name = 'Marks Obtained', blank=True, null=True)
    def __str__(self):
        return self.full_name

# section for aptitude test end ###############################################################################################