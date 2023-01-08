from django.urls import path
from tree_menu import views

urlpatterns = [
    path ('', views.tree_menu, name='tree_menu'),
]