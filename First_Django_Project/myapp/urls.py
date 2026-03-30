from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="Home"),
    path("todos/", views.todos, name="Todos"),
    path("users/", views.users, name="Users"),
    path("todos/<int:id>", views.index, name="index"),
    path("create/", views.create_todoList, name="Create"),
    path("todos/<int:id>/create-item/", views.create_item, name="Create"),
    path("todos/<int:id>/<int:item_id>", views.item, name="Item"),
    path("me/", views.me, name="MyName"),
    path("bootstrap/", views.base_bootstrap, name="Bootstrap Base"),
]
