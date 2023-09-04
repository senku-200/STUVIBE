from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def custom_time_since(value):
    now = timezone.now()
    delta = now - value

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60

    if days > 0:
        return f"{days} days"
    elif hours > 0:
        return f"{hours} hours"
    elif minutes > 0:
        return f"{minutes} minutes"
    else:
        return f"{seconds} seconds"
