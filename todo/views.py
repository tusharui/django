from django.shortcuts import render
from .models import Task 
from .serializers import TaskSerializer , UserSerializer
from  rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.contrib.auth  import authenticate
from rest_framework import generics, permissions

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self , request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username= username , password= password )
        if user:
            refresh = RefreshToken.for_user(user)
            return  Response({'refresh':str(refresh), 'access': str(refresh.access.token)})
        return Response({'error': 'Invalid Credentials'}, status = 400)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user =  self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_query(self):
        return Task.objects.filter(user=self.request.user)