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
class User(models.Model):
    first_name = models.CharField(max_length = 256,verbose_name = 'Full Name')
    email = models.EmailField(max_length = 264,unique = True,verbose_name = 'Email Id.:')
    semester = models.CharField(max_length=1, choices=MY_CHOICES,verbose_name = 'Semester')
    branch = models.CharField(max_length=5, choices=BRANCH,verbose_name = 'Branch')
    link = models.URLField(max_length = 250,verbose_name = 'link')
    skills = models.TextField(max_length = 1000,verbose_name = 'What you Know?:')
    interest = models.TextField(max_length = 1000,verbose_name = 'What are you interested in?:')
    workshop = models.TextField(max_length = 1000,verbose_name = 'Attended any workshop?:')
    contact = models.IntegerField(verbose_name = 'Contact no.:')
