from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()
class PostViewSet(viewsets.ModelViewSet):
    queryset =Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)        

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
        
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Check if the post is already liked by the user
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "Post already liked"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like entry
        Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the like exists
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the like
        like.delete()

        return Response({"detail": "Post unliked"}, status=status.HTTP_204_NO_CONTENT)        