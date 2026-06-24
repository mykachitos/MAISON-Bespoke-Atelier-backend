from rest_framework import serializers

from catalog.models import Product

from .models import Order, OrderItem


class SafeProductRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        if data in (None, ""):
            return None

        try:
            return super().to_internal_value(data)
        except serializers.ValidationError:
            # Frontend can submit demo/local catalog ids that do not exist in the DB yet.
            # We still keep the order itself and rely on editor_data for item details.
            return None


class OrderItemSerializer(serializers.ModelSerializer):
    product = SafeProductRelatedField(
        queryset=Product.objects.all(),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'price', 'editor_data')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'total', 'address', 'created_at', 'items')
        read_only_fields = ('user', 'total', 'created_at')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(user=self.context['request'].user, **validated_data)
        total = 0
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
            total += item['price'] * item['quantity']
        order.total = total
        order.save()
        return order
