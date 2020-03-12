from rest_framework import serializers
from .models import User


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(primary_key=True)
#     username = serializers.CharField(max_length = 100)
#     last_login = serializers.DateTimeField()
#     login_count = serializers.IntegerField()
#     project_count = serializers.IntegerField() 


#     def create(self, validated_data):
#         return User.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.username = validated_data.get('username', instance.username)
#         instance.last_login = validated_data.get('last_login', instance.last_login)
#         instance.login_count = validated_data.get('login_count', instance.login_count)
#         instance.project_count = validated_data.get('project_count', instance.project_count)

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ['id', 'username', 'last_login', 'login_count', 'project_count']