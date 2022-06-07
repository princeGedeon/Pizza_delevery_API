from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
from rest_framework.response import Response


class HelloOrdersView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"},status=status.HTTP_200_OK)