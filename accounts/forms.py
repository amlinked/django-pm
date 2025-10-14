from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm , UserChangeForm 
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
attrs = { "class" : "form-control"}

class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs) :
        super(UserLoginForm , self).__init__( *args, **kwargs)
        
    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(attrs=attrs)
    )        
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs=attrs)
    )    
    
class UserRegistrationForm(UserCreationForm):     
    
    first_name = forms.CharField(
        label=_("First_name"),
        widget=forms.TextInput(attrs=attrs)
    )    
    last_name = forms.CharField(
        label=_("Lastname"),
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(attrs=attrs)
    ) 
    email = forms.CharField(
        label=_("Email"),
        widget=forms.TextInput(attrs=attrs)
    )
       
    password1 = forms.CharField(
        label=_("Password"),
        strip=False , 
        widget=forms.PasswordInput(attrs=attrs)
    )       
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        strip=False , 
        widget=forms.PasswordInput(attrs=attrs)
    )  
    
    class Meta(UserCreationForm.Meta): # type: ignore
        fields = ['first_name', 'last_name' , 'username' , 'email']
        
class ProfileForm(UserChangeForm):
    class Meta:  
        model = User   
        fields = ['first_name' , 'last_name' , 'email']   
        widgets = {
            'first_name':forms.TextInput(attrs=attrs),
            'last_name':forms.TextInput(attrs=attrs),
            'email':forms.EmailInput(attrs=attrs),
        }
          