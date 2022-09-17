from inspect import Attribute
from django import template


register = template.Library()

@register.filter
def model_name(obj):
    """Este é um filtro de template que pode ser aplicado como object|model_name para obter o nome do modelo de um objeto"""
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
