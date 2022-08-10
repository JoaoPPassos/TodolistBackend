from rest_framework import serializers

from .models import Categories, Todo

class CategoriesSerializer(serializers.ModelSerializer):
  # category_name = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Categories
    fields = ["id","nm_category","user_id","color"]

  # def get_category_name(self,obj) :
  #   if not hasattr(obj,'id') or not isinstance(obj,Categories): 
  #     return None
  #   return obj.get_category_name()
  
  
class TodoSerializer(serializers.ModelSerializer):
  # my_priority = serializers.SerializerMethodField()
  
  class Meta:
    model = Todo
    fields = ['title','description','deadline','category','priority','user_id']
    
  # def get_my_priority(self, obj):
  #   return obj.get_my_prority_display()