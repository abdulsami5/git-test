from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    """serializer class for User model"""
    groups = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('uuid', 'username', 'email', 'profile_pic', 'password', 'groups', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
                email=validated_data['email'],
                username=validated_data['email']
        )
        #setting user's password in hash format
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_groups(self, obj):
       return [group.name for group in obj.groups.all()]
