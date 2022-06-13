from django.utils.dateparse import parse_datetime

from django import template

register = template.Library()


@register.simple_tag
def timestamp_to_datetime(timestamp):
    return parse_datetime(timestamp)
