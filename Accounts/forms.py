from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Accounts.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']