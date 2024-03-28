from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_note_items, name="list_notes"),
    path('insert_note/', views.insert_note_item, name="insert_note_item"),
    path('modify_note/<int:note_id>/', views.modify_note_item, name="modify_note_item"),
    path('modify_note_action/<int:note_id>/', views.modify_note_item_action, name="modify_note_item_action"),
    path('delete_note/<int:note_id>/', views.delete_note_item, name="delete_note_item")
]
