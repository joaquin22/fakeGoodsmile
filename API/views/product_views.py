import json
from rest_framework import viewsets
from rest_framework.response import Response
from API.models import Product, Manufacturer, Serie
from API.serializers import ManufacturerSerializer, SerieSerializer, ProductSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def create(self, request):
    #     data = request.data
    #     print(data)
    #     serializer = ProductSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(request.data, status=400)
