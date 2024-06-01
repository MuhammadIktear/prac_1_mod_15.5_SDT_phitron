from django.urls import path

from album import views
from . import views
urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('view/<int:id>/', views.view_musician, name='view_musician'),
    path('edit/<int:id>/', views.edit_musician, name='edit_musician'),
    path('delete/<int:id>/', views.delete_musician, name='delete_musician'),
]