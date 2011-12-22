# encoding: utf-8
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc

register = template.Library()

@register.filter
def factor_class(value):
    klass = 'factor '
    if value == 0:
        klass += 'free'
    elif value <= 75:
        klass += 'low'
    elif value <= 100:
        klass += 'full'
    elif value > 100:
        klass += 'high'
    return klass


@register.simple_tag
def cell(assignments):
    return ''.join(project_div(project) for project in assignments)


def project_div(project):
    d = dict(name=esc(project.name), color=esc(project.color))
    if project.display_as_free:
        return mark_safe('<div class="project %(color)s"></div>' % d)
    else:
        d['url'] = project.get_absolute_url()
        return mark_safe('<a href="%(url)s" class="project %(color)s" title="%(name)s"></a>' % d)

MEMBER_TAG = '<li><a href="%(url)s" class="label %(color)s">%(name)s</a></li>'

@register.simple_tag
def project_members(people):
    html = ['<ul class="unstyled project-members">']
    for person in people:
        d = {'url': esc(person.get_absolute_url()), 'color': esc(person.color),
             'name': esc(person.name)}
        html.append(MEMBER_TAG % d)
    html.append('</ul>')
    return mark_safe('\n'.join(html))
