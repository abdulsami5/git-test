from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import generics, status
from django.contrib.auth.models import Group
import json


@api_view(['POST',])
def register(request):
    """This api endpoint is to register new user"""
    data = json.dumps(request.data)
    data = json.loads(data)
    data['username'] = request.data.get('email')
    user_serializer = UserSerializer(data=data)
    if user_serializer.is_valid(raise_exception=True):
        user=user_serializer.save()
        agent_group = Group.objects.get(name='Agent')
        agent_group.user_set.add(user)
        return Response({"data": user_serializer.data}, status=status.HTTP_201_CREATED)
