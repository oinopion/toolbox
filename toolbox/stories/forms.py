# encoding: utf-8
from django import forms
from django.forms import fields
from stories.models import Story

class StoryImportanceUpdateForm(forms.ModelForm):
    next_pk = fields.IntegerField(required=False, widget=forms.HiddenInput)
    previous_pk = fields.IntegerField(required=False, widget=forms.HiddenInput)
    
    class Meta:
        model = Story
        fields = ()

    def save(self, *args, **kwargs):
        prev = self.cleaned_data['previous_pk']
        next = self.cleaned_data['next_pk']
        self.instance.move_between(prev, next)
        return super(StoryImportanceUpdateForm, self).save(*args, **kwargs)

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ('importance', )
