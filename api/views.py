from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Category,Dish
from .serializer import CategorySerializer,DishSerializer
# Create your views here.

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDishes(request, id):
    try:
        category = Category.objects.get(id=id)
        dishes = Dish.objects.filter(category=category)
    except Category.DoesNotExist:
        dishes = Dish.objects.all()

    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data)

