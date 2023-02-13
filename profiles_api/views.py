from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIVIew features"""
        an_apiview = [
            'uses HTTP methods as functions (get, post, put, patch, delete)'
            'similar to a django view',
            'is mapped manually to a url'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
