from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        labels={'User_ID':'UID','User_name':'Name'}  #tHIS LINE IS USED TO CUSTOMIZE LABEL DISPLAYED ON WEBPAGE
        widgets={'Email':forms.PasswordInput} #Widges are used to change the change the box type 
        

        fields='__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'