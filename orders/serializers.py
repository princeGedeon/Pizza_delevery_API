from rest_framework import serializers

from orders.models import Orders


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=["size","order_status","quantity","customer","active"]

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=["size","order_status","quantity","customer","active","created_at","updated_at"]
