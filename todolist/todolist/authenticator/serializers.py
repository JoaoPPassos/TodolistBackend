from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["username","email","password","birthday"]


class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["username","email","id","token"]
    read_only_fields=['token']
