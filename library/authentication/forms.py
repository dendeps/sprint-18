from django import forms
from django.forms import ModelForm

from authentication.models import CustomUser

'''class CustomUserForm(forms.Form):
    name = forms.CharField(label='Book title', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    count = forms.DecimalField(label='Count', min_value=10)'''

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'role', 'password']

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})