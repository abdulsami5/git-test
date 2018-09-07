from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import generics, status
from django.contrib.auth.models import Group
import json


@api_view(['POST',])
def register(request):
    """This api endpoint registers new user"""
    request_data = json.dumps(request.data)
    request_data = json.loads(request_data)
    user_email = request.data.get('email')
    #As django auth uses username to authenticate users and raven uses
    #emails so users's email is assigned as username to use django's
    #authenticate method.
    request_data['username'] = user_email
    user_serializer = UserSerializer(data=request_data)
    if user_serializer.is_valid(raise_exception=True):
        user = user_serializer.save()
        agent_group = Group.objects.get(name='Agent')
        user.groups.add(agent_group)
        return Response({"message": "User successfuly registered."}, status=status.HTTP_201_CREATED)
