from django.urls import path
from . import views

urlpatterns = [
    path("homeway_property_ltd/", views.homeway, name="Homeway Property LTD"),
    path("homeway_property_ltd/add_new_flat", views.add_flat, name="add_flat"),
    path("homeway_property_ltd/<str:flat_no>-<str:building>", views.flat_details, name="flat_details"),
    path("homeway_property_ltd/cleaners", views.cleaners, name="cleaners"),
    path("homeway_property_ltd/schedule", views.schedule, name="schedule"),
    path("homeway_property_ltd/add_new_cleaner", views.add_cleaner, name="add_cleaner"),
    path("homeway_property_ltd/<str:flat_no>-<str:building>/add_maintenance_note", views.add_edit_maintenance_note, name="add_maintenance_note"),
    path("homeway_property_ltd/<str:flat_no>-<str:building>/edit_maintenance_note_<int:note_id>", views.add_edit_maintenance_note, name="edit_maintenance_note"),
]
