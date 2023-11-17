from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
class PostList(viewsets.ModelViewSet):
   #  permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    # вернуть пост который соответствует запросу т.е. slug == запросу
    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()