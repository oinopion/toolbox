# encoding: utf-8
from collections import defaultdict
from datetime import timedelta, date
from itertools import groupby
from operator import attrgetter
from dateutil.relativedelta import relativedelta, MO
from toolbox.workload.models import Project
from toolbox.people.models import Person

class DailySchedule(object):
    def __init__(self, date_range):
        self.date_range = date_range
        self.dates = defaultdict(list)

    def add(self, assignment):
        date = assignment.date
        self.dates[date].append(assignment.project)

    def __iter__(self):
        for date in self.date_range:
            yield date, self.dates[date]


class PersonSchedule(DailySchedule):
    pass


class ProjectSchedule(DailySchedule):
    def add(self, assignment):
        date = assignment.date
        self.dates[date].append(assignment.person)


class NonProject(object):
    display_as_free = True
    
    def __init__(self, name='Free', color='color-0'):
        self.name = name
        self.color = color


class WeeklySchedule(object):
    def __init__(self, weeks_range):
        self.weeks_range = weeks_range
        self.date_range = [w[0] for w in self.weeks_range]
        self.dates = defaultdict(list)

    def add(self, assignment):
        date = assignment.date
        self.dates[date].append(assignment.project)

    def __iter__(self):
        np = NonProject()
        for week in self.weeks_range:
            projects = list()
            for day in week:
                day_assignments = self.dates[day]
                if not day_assignments and np not in projects:
                    projects.append(np)
                projects.extend(p for p in day_assignments if p not in projects)
            yield week[0], projects


class WeeklyProjectSchedule(WeeklySchedule):
    def add(self, assignment):
        date = assignment.date
        self.dates[date].append(assignment.person)

    def __iter__(self):
        for week in self.weeks_range:
            people = set()
            for day in week:
                day_assignments = self.dates[day]
                people.update(day_assignments)
            yield week[0], sorted(people, key=lambda person: person.name)


class WeeklyGrid(object):
    def __init__(self, start, weeks, queryset):
        self.weeks_range = weeks_range(start, weeks)
        self.date_range = [w[0] for w in self.weeks_range]
        self.assignments = defaultdict(self.single_schedule)
        q = queryset.filter(date__gte=self.weeks_range[0][0])
        q = q.filter(date__lte=self.weeks_range[-1][-1])
        self.people = Person.objects.all()

        for assignment in q:
            self.add(assignment)

    def add(self, assignment):
        person = assignment.person
        self.assignments[person].add(assignment)

    def single_schedule(self):
        return WeeklySchedule(self.weeks_range)

    def __iter__(self):
        for person in self.people:
            yield person, self.assignments[person]


class WeeklyProjectGrid(WeeklyGrid):
    def __init__(self, start, weeks, queryset):
        super(WeeklyProjectGrid, self).__init__(start, weeks, queryset)
        self.projects = Project.objects.all()

    def single_schedule(self):
        return WeeklyProjectSchedule(self.weeks_range)

    def add(self, assignment):
        self.assignments[assignment.project].add(assignment)

    def __iter__(self):
        for project in self.projects:
            yield project, self.assignments[project]


class WorkloadGrid(object):
    schedule_class = PersonSchedule

    def __init__(self, start, end, queryset):
        self.date_range = date_range_inclusive(start, end,
                                               exclude_weekends=True)
        self.assignments = defaultdict(self.single_schedule)
        self.people = Person.objects.all()
        for assignment in queryset.filter(date__gte=start).filter(
            date__lte=end):
            self.add(assignment)

    def add(self, assignment):
        person = assignment.person
        self.assignments[person].add(assignment)

    def single_schedule(self):
        return self.schedule_class(self.date_range)

    def __iter__(self):
        for person in self.people:
            yield person, self.assignments[person]


class ProjectloadGrid(WorkloadGrid):
    schedule_class = ProjectSchedule

    def __init__(self, start, end, queryset):
        super(ProjectloadGrid, self).__init__(start, end, queryset)
        self.projects = Project.objects.all()

    def add(self, assignment):
        project = assignment.project
        self.assignments[project].add(assignment)

    def __iter__(self):
        for project in self.projects:
            yield project, self.assignments[project]


class BaseDetailGrid(object):
    ONE_DAY = timedelta(days=1)
    WEEKEND = timedelta(days=3)
    key = None

    def __init__(self, project):
        self.project = project
        self.assignments = project.assignment_set.order_by('date').select_related('person')
        self.dates = []
        self.prepare()

    def prepare(self):
        last_date = None
        for date, assignments in groupby(self.assignments, key=lambda a: a.date):
            sep = self.separator(last_date, date)
            if sep:
                self.dates.append(sep)
            self.dates.append((date, [self.key(a) for a in assignments]))
            last_date = date

    def separator(self, previous, next):
        if previous is None:
            return None
        delta = next - previous
        if delta == self.ONE_DAY:
            return None
        if self.is_weekend(delta, previous):
            return 'separator', 'weekend'
        return 'separator', delta.days

    def is_weekend(self, delta, previous):
        return delta == self.WEEKEND and previous.weekday() == 4

            
    def __iter__(self):
        return iter(self.dates)


class ProjectGrid(BaseDetailGrid):
    key = attrgetter('person')


class PersonGrid(BaseDetailGrid):
    key = attrgetter('project')


def date_xrange_inclusive(start, end, exclude_weekends=False):
    assert start <= end
    one_day = timedelta(days=1)
    current = start
    while current <= end:
        if exclude_weekends and current.weekday() > 4: # 5 - sat, 6 - sun
            pass
        else:
            yield current
        current = current + one_day


def date_range_inclusive(start, end, exclude_weekends=False):
    return tuple(date_xrange_inclusive(start, end, exclude_weekends))


def weeks_range(start, weeks=4):
    current_date = start
    range = []
    for w in xrange(weeks):
        monday = current_date + relativedelta(weekday=MO(-1))
        friday = monday + timedelta(days=4)
        range.append(date_range_inclusive(monday, friday))
        current_date = current_date + timedelta(days=7)
    return range

