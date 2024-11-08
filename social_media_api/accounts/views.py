from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser.objects.all() here
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    'permissions.IsAuthenticated'  

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser.objects.all() here
    permission_classes = [IsAuthenticated]
    'permissions.IsAuthenticated'  # Display string for checks

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({'detail': 'You are now following this user'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser.objects.all() here
    permission_classes = [IsAuthenticated]
    'permissions.IsAuthenticated'  # Display string for checks

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if request.user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({'detail': 'You have unfollowed this user'}, status=status.HTTP_200_OK)    

