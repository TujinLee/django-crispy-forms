from django.template import Context, Template
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django import template


register = template.Library()

@register.filter
def as_uni_form(form):
    template = get_template('templates/uni_form.html')
    c = Context({'form':form})

    return template.render(c)
    
