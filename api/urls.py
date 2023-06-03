from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.getCategories,name="getCategories"),
    path('categories/<int:id>',views.getDishes,name="getDishes"),
]