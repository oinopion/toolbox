# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from stories.forms import StoryImportanceUpdateForm, StoryForm
from stories.models import Story

class StoriesListView(ListView):
    template_name = 'stories/stories_list.html'
    context_object_name = 'stories_list'


    def get_queryset(self):
        return Story.objects.order_by('-importance')


    def get_context_data(self, **kwargs):
        context = super(StoriesListView, self).get_context_data(**kwargs)
        context['importance_form'] = StoryImportanceUpdateForm()
        return context


class ImportanceUpdateView(UpdateView):
    form_class = StoryImportanceUpdateForm
    model = Story

    def get_success_url(self):
        return reverse('stories_list')


class StoryCreationView(UpdateView):
    form_class = StoryForm
    model = Story

    def get_success_url(self):
        return reverse('stories_list')


stories_list = StoriesListView.as_view()
importance_update = ImportanceUpdateView.as_view()

