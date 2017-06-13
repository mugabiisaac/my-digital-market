from django import template

register = template.Library()

from ..models import Product, THUMB_CHOICES

@register.filter
def get_thumbnail(obj, arg):
    """
    obj == Product instance

    """
    
    return obj.thumbnail_set.filter(type=arg).first().media.url
