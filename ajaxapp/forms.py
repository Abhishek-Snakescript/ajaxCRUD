from dataclasses import fields
from django import forms 
from .models import UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserReg(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['name','number','adress']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","id":"name"}),
            'number':forms.TextInput(attrs={"class":"form-control","id":"number"}),
            'adress':forms.TextInput(attrs={"class":"form-control","id":"adress"}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


