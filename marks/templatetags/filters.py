from django import template

register = template.Library()

@register.filter(name='sessional_filter')
def sessional_filter(queryset, sessional_index):
    return queryset.filter(sessional_index=sessional_index)
