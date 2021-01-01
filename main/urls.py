from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show_input),
    path('shows/create', views.create_new_show),
    path('shows/<show_id>', views.display_show_info),
    path('shows/<show_id>/edit', views.edit_show_input),
    path('shows/<show_id>/save-edit', views.make_edit),
    path('shows/<show_id>/destroy', views.delete_show),
    path('shows', views.all_show),

]