          # -*- coding: utf-8 -*-
from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(label='Имя*', error_messages={'required':'Имя обязательно для заполнения'})
    phone = forms.CharField(label='Телефон*', error_messages={'required':'Телефон обязателен для заполнения'})
    email = forms.EmailField(required=False)
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'2'}), label='Адрес')
