          # -*- coding: utf-8 -*-
from django import forms
from models import Client, DELIVERY_CHOICES

class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput( attrs={u'placeholder': u'Имя*', u'class': u'textInput',}))
    phone = forms.CharField(max_length=255, required=True, widget=forms.TextInput( attrs={u'placeholder': u'Телефон*', u'class': u'textInput',}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput( attrs={u'placeholder': u'Email*', u'class': u'textInput',}))
    address = forms.CharField(max_length=255, required=False, widget=forms.TextInput( attrs={u'placeholder': u'Адрес', u'class': u'textInput',}))
    delivery = forms.ChoiceField(required=False, choices=DELIVERY_CHOICES, widget=forms.RadioSelect)
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={u'class': u'textarea'}))

    class Meta:
        model = Client
        exclude = ('cart',)
