from typing import Union

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def split_string(string_):
    return " • ".join(string_.split(','))
