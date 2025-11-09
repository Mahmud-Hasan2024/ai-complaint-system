from django import template

register = template.Library()

@register.filter(name='in_group')
def in_group(user, group_name):
    """Return True if the user is in the specified group."""
    return user.groups.filter(name=group_name).exists()
