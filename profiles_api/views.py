from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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