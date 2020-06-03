from django.contrib.auth.models import User
from django import forms

class UserRegistration(forms.ModelForm):
    password=forms.forms.CharField( max_length=15, required=True,Widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name','user_name','email','password') 