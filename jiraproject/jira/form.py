from django import forms
from.models import Company,Project,user1,Modules
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea


class NameForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class Projectform(forms.ModelForm):
    class Meta:
        model = Project
        fields='__all__'

#class employeeform(forms.ModelForm):
   # class Meta:
      #  model = Employee
       # fields='__all__'

class userform1(UserCreationForm):
    #password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=user1
        fields='__all__'

class moduleform(forms.ModelForm):
    class Meta:
        model=Modules
        fields = '__all__'

#class login(forms.ModelForm):
     #   model=user1
      #  fields=['username','password']
