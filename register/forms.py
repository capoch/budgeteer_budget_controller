from django import forms
from .models import Entry
from django.contrib.admin import widgets
from django.utils import timezone

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('date','amount', 'currency','category','comments')
