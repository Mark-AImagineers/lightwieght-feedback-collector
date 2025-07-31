from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import EmailUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = EmailUser
        fields = ("first_name", "last_name", "email", "password1", "password2")