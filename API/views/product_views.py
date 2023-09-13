from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from API.models import Product, Manufacturer, Serie
from API.serializers import ManufacturerSerializer, SerieSerializer, ProductSerializer
from API.permissions import IsAdminAuth


class ManufacturerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminAuth]

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
