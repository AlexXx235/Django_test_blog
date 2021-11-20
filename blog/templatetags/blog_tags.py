from django import template
from blog.models import *
from blog.views import *

register = template.Library()


@register.simple_tag()
def get_header_menu():
    return header_menu

@register.simple_tag()
def get_articles():
    return Article.objects.all()