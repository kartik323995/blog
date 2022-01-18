from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 
from .models import profile

class  registration_form(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class  profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']  

class  user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email',]

