from django import template

from tree_menu.models import Menu

register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name):
    menu_items = Menu.objects.filter(name=menu_name)
    return {'menu_items': menu_items}