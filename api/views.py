from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, decorators
from .serializers import ProductSerializer, CateogrySerializer
from main.models import Product, Category
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from .paginations import CustomPagination


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    @decorators.action(methods=["patch", "put"], detail=True, url_name="update_stock")
    def update_stock(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        if product.in_stock:
            product.in_stock = False
        else:
            product.in_stock = True
        product.save()
        return Response({"detail": "Product in_stock updated!"})

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CateogrySerializer



