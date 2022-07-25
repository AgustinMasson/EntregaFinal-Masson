from django import forms
from django.contrib.auth.forms import UserCreationForm, User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Username")
    email = forms.EmailField(label="E-Mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    lastname = forms.CharField(label="Last Name")
    firstname = forms.CharField(label="First Name")
    nationality = forms.CharField(label="Nationality")
    team = forms.CharField(label="Favourite Team")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "lastname", "firstname", "nationality", "team"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="E-Mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    lastname = forms.CharField(label="Last Name")
    firstname = forms.CharField(label="First Name")
    nationality = forms.CharField(label="Nationality")
    team = forms.CharField(label="Favourite Team")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "lastname", "firstname", "nationality", "team"]
        help_texts = {k:"" for k in fields}