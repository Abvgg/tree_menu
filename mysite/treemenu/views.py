from django.shortcuts import render


def menu_items(request):
    return render(request, 'treemenu/menu_items.html', {})