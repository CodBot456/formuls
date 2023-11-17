from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
 #   owner=serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Post
        fields = ['name','value','units','owner','id']
