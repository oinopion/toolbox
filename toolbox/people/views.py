from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from toolbox.people.models import Person

class PeopleListView(ListView):
    context_object_name = 'people_list'
    template_name = 'people/people_list.html'
    queryset = Person.objects.all()


class PersonDetailView(DetailView):
    context_object_name = 'person'
    model = Person
    template_name = 'people/person_detail.html'


people_list_view = PeopleListView.as_view()
person_detail_view = PersonDetailView.as_view()
