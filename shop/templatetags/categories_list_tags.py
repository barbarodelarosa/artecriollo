from django import template
from shop.models import Category
from django.db.models import Count


register = template.Library()

@register.simple_tag()
def categories_list_tag():
    categories = Category.objects.all()
    return categories



@register.simple_tag()
def categories_list_for_footer():
    count_posts = Category.objects.annotate(num_products=Count('product')).order_by('-num_products')
    return count_posts[:6]

  