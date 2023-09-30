from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password2', 'password2']