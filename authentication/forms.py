from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from requests import request

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User doesn't exist")
            if not user.check_password:
                raise forms.ValidationError("Incorrect Password")
        return super(LoginForm, self).clean(*args, **kwargs)

class RegistrationUserEmail(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    email = forms.EmailField(required=True ,max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
# class RegistrationUserMobileNo(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='Optional')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Optional')
#     mobile = forms.NumberInput(request=True)

#     class Meta:
#         model = User
#         fields = [
#             'username', 
#             'first_name', 
#             'last_name', 
#             'mobile', 
#             'password1', 
#             'password2', 
#             ]