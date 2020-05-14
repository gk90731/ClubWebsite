from django import forms
from appTwo.models import tech_team,org_team,Staff,Sudent_choice,notice_tech,notice_org

class NewUserForm(forms.ModelForm):
    class Meta():
        model = tech_team
        fields = ('first_name','email','semester','branch','link','skills','interest','workshop','contact',)
class NewUserForm_new(forms.ModelForm):
    class Meta():
        model = org_team
        fields = ('first_name','email','semester','branch','link','skills','interest','workshop','contact',)
class ContactForm(forms.Form):
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)

class StaffForm(forms.ModelForm):
    class Meta():
        model = Staff

        fields = '__all__'
class Sudent_choiceForm(forms.ModelForm):
    class Meta():
        model = Sudent_choice

        fields = '__all__'



class Notice_Tech(forms.ModelForm):
    class Meta():
        model = notice_tech
        fields = '__all__'
class Notice_Org(forms.ModelForm):
    class Meta():
        model = notice_org
        fields = '__all__'
