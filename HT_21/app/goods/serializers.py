from rest_framework import serializers

from .models import Guitar, CategoryOfGuitar


class GoodsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    price = serializers.IntegerField(min_value=0)
    count = serializers.IntegerField(min_value=0)
    description = serializers.CharField()
    path_img = serializers.FileField(default='')
    products_id = serializers.IntegerField()

    def create(self, validated_data):
        return Guitar.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.count = validated_data.get('count', instance.count)
        instance.description = validated_data.get('description', instance.description)
        instance.products_id = validated_data.get('products_id', instance.products_id)
        instance.save()
        return instance


class CatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)

    def create(self, validated_data):
        return CategoryOfGuitar.objects.create(**validated_data)
