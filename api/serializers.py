from .models import Post,Category
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
 #   owner=serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Post
        fields = ['name','value','units','owner','id',"category"]


class CategorySerializer(serializers.ModelSerializer):
    posts=PostSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ["title", "posts"]