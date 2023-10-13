from django import template
from treemenu.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)

    print(menu_items)  # Отладочный вывод

    def render_menu(menu_items):
        result = '<ul>'
        for item in menu_items:
            result += f'<li><a href="{item.url or item.named_url}">{item.title}</a>'
            children = item.children.all()
            if children:
                result += render_menu(children)
            result += '</li>'
        result += '</ul>'
        return result

    return mark_safe(render_menu(menu_items))

