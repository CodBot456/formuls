from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=200,default="")
    value=models.TextField(default="")
    units=models.TextField(default="")
    owner=models.ForeignKey("auth.User",related_name="posts",on_delete=models.CASCADE)
# Create your models here.
