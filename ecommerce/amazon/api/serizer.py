from rest_framework import serializers
from amazon.models import Product


class productSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    category =  serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=150)
    img = serializers.ImageField()
    
    def create(self,validates_data):
      return  Product.objects.create(validates_data)
  
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.price = validated_data.get('price')
        instance.category = validated_data.get('category')
        instance.image = validated_data.get('image')
        instance.img = validated_data.get('img')
        instance.save()
        return instance