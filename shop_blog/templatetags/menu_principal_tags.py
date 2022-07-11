from django import template
from shop_blog.models import Categoria
register = template.Library()




from django.db.models import Count
@register.simple_tag()
def menu_principal():
    menu_list = Categoria.objects.annotate(count=Count('post')).order_by('count')[:5]
    return menu_list



