from django import  forms
from django.contrib.auth.management.commands.createsuperuser import PASSWORD_FIELD
from django.forms import PasswordInput

JOBS = (
    ("python", "développeur Python"),
    ("javascript", "développeur Javascript"),
    ("flutter", "développeur Flutter")
)
class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=10, required=False, strip=True, )
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
  
