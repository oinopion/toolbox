from django.db import models
from toolbox.workload.models import Project

TOP = 1.0
BOTTOM = 0.0

class Story(models.Model):
    text = models.TextField()
    description = models.TextField(blank=True)
    estimate = models.PositiveSmallIntegerField(blank=True, null=True)
    importance = models.FloatField()

    class Meta:
        ordering = ['-importance']
        verbose_name_plural = 'Stories'

    def move_between(self, previous_pk, next_pk):
        next = get_importance_or_default(next_pk, 0.0)
        previous = get_importance_or_default(previous_pk, 1.0)
        self.importance = (previous + next) / 2.0
        if previous - next < 0.0000001:
            self._needs_recalc = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.importance = last() / 2.0
        super(Story, self).save(*args, **kwargs)
        if hasattr(self, '_needs_recalc'):
            stories = Story.objects.order_by('importance')
            step = TOP / (len(stories) + 1)
            for i, story in enumerate(stories):
                story.importance = step * (i+1)
                story.save()



def get_importance_or_default(pk, default):
    try:
        return Story.objects.get(pk=pk).importance or default
    except Story.DoesNotExist, Story.MultipleObjectsReturned:
        return default

def last():
    try:
        return Story.objects.order_by('importance')[0].importance
    except (Story.DoesNotExist, IndexError):
        return 1.0

