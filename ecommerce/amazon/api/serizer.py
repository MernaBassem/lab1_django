from rest_framework import serializers
from category.models import Category

class productSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    category =  serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=150)
    img = serializers.ImageField()
