from rest_framework import serializers

from API.models import Manufacturer, Serie, Product, ProductImage


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "manufacturer",
            "serie",
            "specifications",
            "release_date",
            "images",
        ]

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        image_data = self.context["request"].data.getlist("images")
        if image_data:
            for image in image_data:
                ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        images_data = self.context["request"].data.getlist("images")
        if images_data:
            instance.images.clear()
            for image in images_data:
                product_image = ProductImage.objects.create(image=image)
                instance.images.add(product_image)

        instance = super().update(instance, validated_data)
        instance.save()
        return instance
