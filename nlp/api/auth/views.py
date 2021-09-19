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
            user = register_serializer.save()
            resp = {
                "email": user.email,
                "room": user.id
            }
            
            return Response(resp, status=200)
        
        return Response(register_serializer.errors, status=400)


class LoginView(generics.CreateAPIView):
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        
        if login_serializer.is_valid():
            user = login_serializer.save()
            resp = {
                "email": user.email,
                "room": user.id
            }
            
            return Response(resp, status=200)
        
        return Response(login_serializer.errors, status=400)
