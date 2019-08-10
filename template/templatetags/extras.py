from django import template


register = template.Library()


@register.filter
def inc(value, args):
    """
    :param value:
    :param args:
    :return: increment value plus args
    """
    return int(value) + int(args)

@register.simple_tag
def division(a, b, to_int=False):
    """
    :param a: int or float
    :param b: int or float
    :param to_int: True or False
    :return:
    """
    if to_int:
        return int(a) // int(b)
    return int(a) / int(b)
