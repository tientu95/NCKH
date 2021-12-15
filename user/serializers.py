from rest_framework import serializers
from .models import User

class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id',)
class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user_mail = serializers.CharField(max_length=50)
    user_pass = serializers.CharField(max_length=50)
    user_name = serializers.CharField(max_length=50)
    user_phone = serializers.CharField(max_length=10)
    decent = serializers.IntegerField()
