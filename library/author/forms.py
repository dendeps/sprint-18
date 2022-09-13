from django import forms
from django.forms import ModelForm
from .models import Author
from django.core.exceptions import ValidationError
import datetime

class AuthorForm(ModelForm):

    class Meta:
        model=Author
        fields=('name', 'surname','patronymic')
        labels = {'name': ('Name'),'surname': ('Surname'),'patronymic': ('Patronymic')}





