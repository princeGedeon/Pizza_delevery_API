from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from orders.models import Orders
from orders.serializers import OrderCreationSerializer


class HelloOrdersView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"},status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Orders.objects.all()