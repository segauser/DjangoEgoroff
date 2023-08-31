
from django import template
from django.template.defaultfilters import stringfilter # гарантирует что value будет str

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)