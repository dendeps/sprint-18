from django import forms
from django.forms import ModelForm, ModelChoiceField
from order.models import Order
from book.models import Book
from authentication.models import CustomUser


class CustomUserField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.email


class BookField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class OrderForm(ModelForm):
    user = CustomUserField(queryset=CustomUser.objects.all(), empty_label="Select user")
    book = BookField(queryset=Book.objects.all(), empty_label="Select book")

    class Meta:
        model = Order
        fields = ['user', 'book', 'plated_end_at']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['book'].widget.attrs.update({'class': 'form-control'})
        self.fields['plated_end_at'].widget.attrs.update({'class': 'form-control'})