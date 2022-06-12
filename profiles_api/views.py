from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of  API view features"""
        an_apiview = [
            'Uses http method as function (get,post,patch,put,delete) ',
            'Is similiar to traditional DjangoView',
            'Gives you most control over your app logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
