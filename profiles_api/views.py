from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerialzier

    def get(self, request, format=None):
        """Return a list of APIVIew features"""
        an_apiview = [
            'uses HTTP methods as functions (get, post, put, patch, delete)'
            'similar to a django view',
            'is mapped manually to a url',
            'APIView are ideal when modifying data on several models(tables) or calling an API inside it'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            data = {
                'message': f"Hello {name}, welcome to my django tutorial"
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating of an objet"""
        return Response({'message': "i am Put"})

    def patch(self, request, pk=None):
        """Handle partial updating of an objet"""
        return Response({'message': "i am Patch"})

    def delete(self, request, pk=None):
        """Handle delete  of an objet"""
        return Response({'message': "i am Delete"})


class HelloViewSet(viewsets.ViewSet):
    """ViewSet class to test viewsets"""
    serializer_class = serializers.HelloSerialzier

    def list(self, request):
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update, destroy)'
            'is mapped automatically to a url',
            'Provides more functionality with more code'
        ]
        return Response({'message': a_viewset})

    def create(self, request):
        """Create a hello world message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            data = {
                'message': f"Hello {name}, welcome to my django viewsets"
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting an object"""
        return Response({'message' : 'GET'})
    
    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({'message' : 'PUT'})
    
    def partial_update(self, request, pk=None):
        """handle partial_update an object"""
        return Response({'message' : 'PATCH'})

    def destroy(self, request, pk=None):
        """handle destroy an object"""
        return Response({'message' : 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle CRUD for user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """CRUD for profile feet items"""
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
