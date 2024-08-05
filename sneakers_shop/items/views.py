from django.shortcuts import render
from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemsAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

