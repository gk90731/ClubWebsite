from django import forms
from appTwo.models import tech_team,org_team,notice_tech,notice_org

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

class Notice_Tech(forms.ModelForm):
    class Meta():
        model = notice_tech
        fields = '__all__'
class Notice_Org(forms.ModelForm):
    class Meta():
        model = notice_org
        fields = '__all__'
