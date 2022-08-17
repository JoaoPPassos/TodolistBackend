import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import generics,permissions
from .serializers import CategoriesSerializer, TodoSerializer
from .models import Categories, Todo
from authenticator.jwt import JWTAuthentication
from authenticator.models import User
from rest_framework.exceptions import APIException


class CategoryCreateAPIView(generics.CreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  serializer_class= CategoriesSerializer
  
  def perform_create(self,serializer):
    name = serializer.validated_data.get("nm_category")
    col = serializer.validated_data.get("color")
    user = self.request.user
    already_has_category = Categories.objects.filter(nm_category = name)
    if already_has_category.exists() and already_has_category.get().user_id == user.id:
      raise APIException("Category already exist")
  
    if name: 
      serializer.save(nm_category = name,user_id = user.id,color = col)  
   
create_category_view = CategoryCreateAPIView.as_view()
    
class CategoryListAPIView(generics.ListAPIView):
  permissions_classes=(permissions.IsAuthenticated,)
  serializer_class = CategoriesSerializer
  
  def list(self,request):
    user_id = request.user.id
    query = Categories.objects.filter(user_id = user_id)
    data = {"data":
      [
        {
          "name":entry.nm_category,
          "user": entry.user_id,
          "id": entry.id,
          "color": entry.color,
        } 
        for entry in query
      ]
    }
    return JsonResponse(data)
    
list_category_view= CategoryListAPIView.as_view()

class TodoCreateAPIView(generics.CreateAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  serializer_class= TodoSerializer
  
  def perform_create(self,serializer):
    description = serializer.validated_data.get("description")
    user = self.request.user

    serializer.save(user_id = user.id)
    if not description: 
      serializer.save(description = "")  
      
create_todo_view = TodoCreateAPIView.as_view()

class TodoListAPIView(generics.ListAPIView):
  permissions_classes=(permissions.IsAuthenticated,)
  serializer_class = TodoSerializer
  
  def list(self,request):
    user_id = request.user.id
    query = Todo.objects.filter(user_id = user_id)
    data = {"data":
      [
        {
          "title":entry.title,
          "description": entry.description,
          "id": entry.id,
          "priority": {
            'nm_priority': entry.get_priority_display(),
            'id': entry.priority,
          },
          "category":{
            'color': entry.category.color,
            'nm_category': entry.category.nm_category,
            'id': entry.category.id
          },
          'deadline': entry.deadline,
        } 
        for entry in query
      ]
    }
   
    return JsonResponse(data)
    
list_todo_view= TodoListAPIView.as_view()


class TodoUpdateAPIView(generics.UpdateAPIView):
  permissions_classes=(permissions.IsAuthenticated,)
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()
  
  def perform_update(self, serializer):
    # params = self.request.data
    serializer.save() 
    
update_todo_view = TodoUpdateAPIView.as_view()

