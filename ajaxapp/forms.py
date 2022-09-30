
from django import forms 
from .models import UserModel


class UserReg(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['name','number','adress']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","id":"name"}),
            'number':forms.TextInput(attrs={"class":"form-control","id":"number"}),
            'adress':forms.TextInput(attrs={"class":"form-control","id":"adress"}),
        }