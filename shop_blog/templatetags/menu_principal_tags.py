from django import template
from shop_blog.models import Categoria
register = template.Library()




from django.db.models import Count
@register.simple_tag()
def menu_principal():
    menu_list = Categoria.objects.annotate(count=Count('post__set__id')).order_by('count')
    # menu_list = Categoria.objects.all()
    return menu_list



