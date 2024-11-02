from django.urls import path
from .views import MenuItemsView, SingleMenuItemsView

urlpatterns = [
    path('menu/',MenuItemsView.as_view()),
    path('menu/<int:pk>',SingleMenuItemsView.as_view()),




]