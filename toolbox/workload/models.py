from django.db import models
from people.models import Person

class Project(models.Model):
    name = models.CharField(max_length=250)

    display_as_free = False
    
    def __unicode__(self):
        return self.name

    @property
    def color(self):
        m = (self.id % 7) + 1
        return 'color-%d' % m


class Assignment(models.Model):
    project = models.ForeignKey(Project)
    person = models.ForeignKey(Person)
    date = models.DateField()

    def __unicode__(self):
        return "(%s) %s in %s" % (self.date, self.person, self.project)

