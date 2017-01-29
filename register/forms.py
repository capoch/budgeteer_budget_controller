from django import forms
from .models import Entry, Category
from django.contrib.admin import widgets
from django.utils import timezone

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('date','amount', 'currency','category','comments')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category_name', 'category_desc')
