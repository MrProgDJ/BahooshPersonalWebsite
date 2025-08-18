from django import forms
from .models import ContactMeModel


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeModel
        fields = ['full_name', 'email', 'subject', 'body']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی خود را وارد کنید',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل خود را وارد کنید',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع را وارد کنید',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام مورد نظر را وارد کنید',
            }),
        }
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادکی اجباری است. لطفا ان را وارد کنید'
            }
        }
