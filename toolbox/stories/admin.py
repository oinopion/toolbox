# encoding: utf-8
from django.contrib import admin
from stories.models import Story

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('text', 'estimate', 'importance')
    readonly_fields = ('importance', )

admin.site.register(Story, StoriesAdmin)
