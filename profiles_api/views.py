from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """ Test API View ! """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """ Return a list of APIView features """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django views',
            'Gives you the most control over your application',
            'Is mapped mannually to URLs'
        ]

        return Response({'messages': 'Hello!', 'an_apiview' : an_apiview})

    def post(self, request):
        """ Create a Hello message with our name """ 
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messege = f'Hello {name}'

            return Response({'messages': messege})

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def  put(self, request, pk=None):
        """ Handle updating an objects """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle partial updating an objects """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """ 

    serializer_class = serializers.HelloSerializer


    def list(self, request):

        """ Return a Hello Messege """ 

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update )',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset' : a_viewset})

    def create(self, request):
        """ Create a Hello Message """ 

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)         

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handling part of an object """
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle destroying/removing an object """        
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating user profile """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
