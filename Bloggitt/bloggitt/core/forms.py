from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile, Post
ALLOWED_DOMAIN = 'psgtech.ac.in'

class SignupForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@' + ALLOWED_DOMAIN):
            raise ValidationErr('Invalid email domain. Please use an email address from ' + ALLOWED_DOMAIN)
        return email
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',  
            'email',
            'password', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets={

            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'body':forms.Textarea(attrs={'class' : 'form-control'})

        }