from django.shortcuts import render
from tree_menu.models import Menu


def tree_menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'base.html', {'menu_items': menu_items})
