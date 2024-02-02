from django.db import models


class Category(models.Model):
    category_options=[
        ("base","base"),
        ("давление твёрдых тел, жидкостей и газов","давление твёрдых тел, жидкостей и газов"),
        ("давление","давление"),
        ("тепловые явления","тепловые явления"),
        ("электрические явления","электрические явления"),
        ("электромагнитные явления","электромагнитные явления"),
        ("световые явления","световые явления"),
        ("законы взаимодействия и движения тел","законы взаимодействия и движения тел"),
        ("электромагнитное поле","электромагнитное поле"),
        ("строение атома и атомного ядра","строение атома и атомного ядра"),
    ]
    title=models.CharField(max_length=200,unique=True,choices=category_options)
    def __str__(self):
        return self.title
    

    
class Post(models.Model):
    name=models.CharField(max_length=200,default="")
    value=models.TextField(default="")
    units=models.TextField(default="")
    owner=models.ForeignKey("auth.User",related_name="posts",on_delete=models.CASCADE)
    category=models.ForeignKey( Category, to_field="title", on_delete=models.PROTECT)
# Create your models here.

    