from rest_framework import serializers

from orders.models import Orders


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=["size","order_status","quantity","customer"]