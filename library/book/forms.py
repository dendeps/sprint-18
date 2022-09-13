from django import forms
from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError
import datetime



class BookForm(ModelForm):

    class Meta:
        model=Book
        fields=('name', 'description','count','year','issue_date','authors')
        labels = {'name': ('Name'),'description': ('Book description'),\
                  'count': ('Book quantity'),'year': ('Year'),'issue_date': ('Issue date'),'author': ('Author')}
