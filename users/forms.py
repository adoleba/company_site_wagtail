from django import forms
from django.forms import DateInput

from wagtail.users.forms import UserEditForm, UserCreationForm


SEX_CHOICES = (
    ('K', 'Kobieta'),
    ('M', 'Mężczyzna'),
)


class CustomUserCreationForm(UserCreationForm):
    country = forms.CharField(required=False)
    birth_date = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    sex = forms.CharField(max_length=1, widget=forms.Select(choices=SEX_CHOICES), required=False)
    about = forms.CharField(widget=forms.Textarea())


class CustomUserEditForm(UserEditForm):
    country = forms.CharField(required=False)
    birth_date = forms.DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    sex = forms.CharField(max_length=1, widget=forms.Select(choices=SEX_CHOICES), required=False)
    about = forms.CharField(widget=forms.Textarea())
