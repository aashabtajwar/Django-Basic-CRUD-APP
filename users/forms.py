from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # now specify the model that this form will interact with
        model = User # once this form validates it is going to create a new user
        # now specify the fields that we want to show
        fields = ['username', 'email', 'password1', 'password2']