from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')


class ProductSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source='full_name')
    oldPrice = serializers.DecimalField(
        source='old_price', max_digits=10, decimal_places=2, allow_null=True, required=False
    )
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'fullName', 'fabric', 'style', 'description',
            'price', 'oldPrice', 'rating',
            'color', 'accent', 'pattern', 'tag',
            'image', 'stock', 'is_active',
        )

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url