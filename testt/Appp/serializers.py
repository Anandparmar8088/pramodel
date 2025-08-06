from rest_framework.serializers import ModelSerializer

from .models import product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"
        