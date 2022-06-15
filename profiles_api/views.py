from email import message
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of  API view features"""
        an_apiview = [
            'Uses http method as function (get,post,patch,put,delete) ',
            'Is similiar to traditional DjangoView',
            'Gives you most control over your app logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle  partial updating  of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'User Action (list,create,retrieve,update,partial_update)',
            'Automatically map to URLs using routers',
            'Provide more functionality with less code',
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})
