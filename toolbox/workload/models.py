from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    @property
    def color(self):
        m = (self.id % 7) + 1
        return 'color-%d' % m


class Person(models.Model):
    name = models.CharField(max_length=250)


    class Meta:
        verbose_name_plural = "People"


    def __unicode__(self):
        return self.name

    @property
    def color(self):
        m = (self.id % 7) + 1
        return 'member-color-%s' % m


class AssgnmentsManager(models.Manager):
    def grid(self, start, end):
        pass

    def in_between(self, start, end):
        return self.filter(date__gte=start).filter(date__lte=end)


class Assignment(models.Model):
    project = models.ForeignKey(Project)
    person = models.ForeignKey(Person)
    date = models.DateField()

    def __unicode__(self):
        return "(%s) %s in %s" % (self.date, self.person, self.project)

