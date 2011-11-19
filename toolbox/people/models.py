from django.db import models

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
