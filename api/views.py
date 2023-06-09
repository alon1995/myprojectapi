from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Dish
from .serializer import CategorySerializer, DishSerializer

# Create your views here.


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDishes(request):
    category_id = request.GET.get('category_id')
    if not category_id:
        return Response({'error': 'Category ID is missing'}, status=400)
    
    dishes = Dish.objects.filter(category_id=category_id)
    if not dishes:
            return Response({'error': 'No dishes found for the given category ID'}, status=404)
    else:
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data, status=200)  

    