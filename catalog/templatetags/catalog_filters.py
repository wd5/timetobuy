from django import template
from catalog.models import Section

register = template.Library()

@register.inclusion_tag("tags/menu.html")
def menu(request):
    active_sections = Section.objects.filter(is_active=True)
    return {
        'sections': active_sections,
        'request': request,
}