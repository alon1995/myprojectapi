from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.getCategories, name="getCategories"),
    path('dishes', views.getDishes, name='get_dishes'),
]
