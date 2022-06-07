from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from orders.models import Orders
from orders.serializers import OrderCreationSerializer, OrderDetailSerializer


class HelloOrdersView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"},status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreationSerializer
    detail_serializer=OrderDetailSerializer

    """
    @action(detail=True,methods=['post'])
    def modify_activation(self,request,pk):
        self.get_object().modify_activation()
        return Response()"""


    def get_queryset(self):

        return Orders.objects.all()

    def get_serializer_class(self):

        if self.action=="retrieve":
            return self.detail_serializer
        return self.serializer_class