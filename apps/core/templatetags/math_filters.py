from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Multiplies the value by the argument.
    Usage: {{ value|mul:3 }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter 
def div(value, arg):
    """
    Divides the value by the argument.
    Usage: {{ value|div:2 }}
    """
    try:
        if float(arg) == 0:
            return 0
        return float(value) / float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def sub(value, arg):
    """
    Subtracts the argument from the value.
    Usage: {{ value|sub:5 }}
    """
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def add_int(value, arg):
    """
    Adds the argument to the value (integer version).
    Usage: {{ value|add_int:3 }}
    """
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return 0