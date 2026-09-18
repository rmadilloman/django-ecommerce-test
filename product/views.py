from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        print("you called the GET method for all products!!!")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("you called the GET method for 1 product!!!")
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("you called the POST method!!!")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print("you called the PUT method!!!")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print("you called the PATCH method!!!!")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print("you called the DELETE method!!!!")
        return super().destroy(request, *args, **kwargs)