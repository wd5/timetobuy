from django import template
from catalog.models import Section, BrandsCategory

register = template.Library()

@register.inclusion_tag("tags/menu.html")
def menu(request):
    active_sections = Section.objects.filter(is_active=True)
    brand_cats = BrandsCategory.objects.all()
    return {
        'sections': active_sections,
        'brand_cats': brand_cats,
        'request': request,
}