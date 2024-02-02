from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer,CategorySerializer
from .models import Post,Category
class PostList(viewsets.ModelViewSet):
   #  permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    # вернуть пост который соответствует запросу т.е. slug == запросу
    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()

class CategoryList(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()