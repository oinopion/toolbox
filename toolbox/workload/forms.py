# encoding: utf-8
from django import forms
from django.forms import fields
from toolbox.workload.models import Assignment
from workload.grid import date_range_inclusive

class AssignmentForm(forms.ModelForm):
    beginnig = fields.DateField(
        widget=forms.DateInput(attrs={'class': 'date-picker'}))
    end = fields.DateField(
        widget=forms.DateInput(attrs={'class': 'date-picker'}))
    next = fields.CharField(widget=forms.HiddenInput())


    class Meta:
        exclude = ['date']
        model = Assignment


    def save(self, commit=True):
        dates = date_range_inclusive(self.cleaned_data['beginnig'],
                                     self.cleaned_data['end'],
                                     exclude_weekends=True)
        for date in dates:
            Assignment.objects.create(**{
                'date': date,
                'person': self.cleaned_data['person'],
                'project': self.cleaned_data['project'],
            })
