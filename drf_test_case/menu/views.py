from django.shortcuts import render
from rest_framework import generics
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodListSerializer
from django.db.models import Prefetch

class FoodApiView(generics.ListAPIView):

    serializer_class = FoodListSerializer
    
    def get_queryset(self):
        queryset = Food.objects.filter(is_publish=True)
        category = FoodCategory.objects.filter(food__is_publish=True).distinct().order_by("order_id").prefetch_related(
            Prefetch('food',queryset=queryset))
        return category




