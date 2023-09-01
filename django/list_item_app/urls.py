from django.urls import path
from .views import All_to_do_items, Single_item

urlpatterns = [
    path("add/", All_to_do_items.as_view(), name="add_item"),
    path("", All_to_do_items.as_view(), name="all_items"),
    path("delete/<int:id>", Single_item.as_view(), name="delete_item"),
    path("update/<int:id>", Single_item.as_view(), name="update_item")
]