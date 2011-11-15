import time
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta, MO, FR
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from toolbox.workload.models import Assignment
from toolbox.workload.grid import WorkloadGrid, ProjectloadGrid, WeeklyGrid, WeeklyProjectGrid
from toolbox.workload.forms import AssignmentForm

WEEK = timedelta(days=4)

def workload(request, date_str=None):
    start = closest_monday(parse_date(date_str))
    end = start + WEEK
    grid = WorkloadGrid(start, end, Assignment.objects.select_related())
    next = start + timedelta(days=7)
    prev = start - timedelta(days=7)
    next = reverse('workload_date', args=[next])
    prev = reverse('workload_date', args=[prev])
    form = AssignmentForm(initial={'next': request.path})
    return render(request, 'workload/workload.html', locals())


def monthworkload(request, date_str=None):
    start = closest_monday(parse_date(date_str))
    grid = WeeklyGrid(start, 8, Assignment.objects.select_related())
    next = start + relativedelta(weeks=8)
    prev = start - relativedelta(weeks=8)
    next = reverse('monthworkload_date', args=[next])
    prev = reverse('monthworkload_date', args=[prev])
    form = AssignmentForm(initial={'next': request.path})
    return render(request, 'workload/workload.html', locals())


def projectload(request, date_str=None):
    start = closest_monday(parse_date(date_str))
    end = start + WEEK
    assignments = Assignment.objects.select_related()
    project_grid = ProjectloadGrid(start, end, assignments)
    next = start + timedelta(days=7)
    prev = start - timedelta(days=7)
    next = reverse('projectload_date', args=[next])
    prev = reverse('projectload_date', args=[prev])
    return render(request, 'workload/projectload.html', locals())


def projectmonthload(request, date_str=None):
    start = closest_monday(parse_date(date_str))
    project_grid = WeeklyProjectGrid(start, 8,
                                     Assignment.objects.select_related())
    next = start + relativedelta(weeks=8)
    prev = start - relativedelta(weeks=8)
    next = reverse('projectmonthload_date', args=[next])
    prev = reverse('projectmonthload_date', args=[prev])
    return render(request, 'workload/projectload.html', locals())

def create_assignment(request):
    form = AssignmentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(form.data['next'])
    else:
        return HttpResponse(status=400, content='Deal with it: ' + form.errors)


# helpers

def closest_monday(a_date=None):
    a_date = a_date or date.today()
    return a_date + relativedelta(weekday=MO(-1))


def parse_date(value):
    try:
        return date(*time.strptime(value, "%Y-%m-%d")[:3])
    except (ValueError, TypeError):
        return None
