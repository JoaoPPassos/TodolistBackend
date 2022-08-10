from django.urls import path

from . import views
urlpatterns = [
    path('category/create/',views.create_category_view),
    path('category',views.list_category_view),
    path('create/',views.create_todo_view),
    path('update/<int:pk>',views.update_todo_view),
    path('',views.list_todo_view),
]
