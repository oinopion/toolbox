# encoding: utf-8
from django.contrib import admin
from toolbox.workload import models

class PeopleAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('person', 'project', 'date')
    list_filter = ('person', 'project')
    date_hierarchy = 'date'
    ordering = ('-date', 'person')


admin.site.register(models.Person, PeopleAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Assignment, AssignmentAdmin)
