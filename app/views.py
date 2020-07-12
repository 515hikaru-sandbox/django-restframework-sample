from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializer import GreetingSerializer


class GreetingViewset(ViewSet):

    def list(self, request):
        return Response({'message': 'Hello, World!'})

    def create(self, request):
        serializer = GreetingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'What\'s your name?'})
        name = serializer.data['name']
        return Response({'message': f'Hello, {name}!'})
