from rest_framework import serializers


from api.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            'name', 'price', 'description', 'count', 'is_active',
        )
    