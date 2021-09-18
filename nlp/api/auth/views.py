from django.db.models import query
from .serializers import RegisterSerializer, LoginSerializer

from rest_framework import generics
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        
        if register_serializer.is_valid():
            
            return Response(register_serializer.validated_data, status=200)
        
        return Response(register_serializer.errors, status=400)


class LoginView(generics.CreateAPIView):
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        
        if login_serializer.is_valid():
            
            return Response(login_serializer.validated_data, status=200)
        
        return Response(login_serializer.errors, status=400)
