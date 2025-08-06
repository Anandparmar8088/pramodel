*🚀 Django ModelSerializer API Example

This project demonstrates how to use **Django REST Framework (DRF)** with a **ModelSerializer** to create simple REST APIs for inserting and retrieving data from a model.

---

## 📦 Model: `product`

This is a simple Django model used to store information about a product:

```python
from django.db import models

class product(models.Model):
    name = models.CharField(max_length=50)     # Product name
    age = models.IntegerField()                # Product age (in years)
    disc = models.TextField()                  # Product description
```

---

## 🔄 Serializer: `ProductSerializer`

This `ModelSerializer` automatically maps all model fields to JSON for easy conversion between Django objects and API data.

```python
from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'  # Includes all fields: name, age, disc
```

---

## 🌐 API Views

Using `@api_view` from DRF, we created two endpoints:

### 1. `GET /api/gt/` – Fetch all product data

```python
@api_view(['GET'])
def senddata(request):
    all_data = product.objects.all()
    all_data = ProductSerializer(all_data, many=True)
    return Response({
        "msg": "hello",
        "data": all_data.data
    })
```

### 2. `POST /api/pst/` – Add a new product

```python
@api_view(['POST'])
def getdata(request):
    new_pro = ProductSerializer(data=request.data)
    if new_pro.is_valid():
        new_pro.save()
        return Response({
            "msg": "Data received successfully",
            "data": new_pro.data
        })
    else:
        return Response({
            "msg": "Data not received",
            "errors": new_pro.errors
        }, status=400)
```

---

## 📥 Sample POST JSON

Use this in Postman or any HTTP client to test the POST endpoint:

```json
{
  "name": "Harvester",
  "age": 2,
  "disc": "Used to harvest crops like wheat and rice efficiently."
}
```

---

## 🔁 Summary

| Feature | Description |
|--------|-------------|
| **Model** | Represents product data |
| **Serializer** | Converts model to JSON and vice versa |
| **GET API** | Returns all product entries in JSON |
| **POST API** | Accepts JSON and creates a new product |
| **DRF** | Makes API creation easy and clean |

---

## 🛠 Future Improvements (Optional)

- Add validation (e.g., age must be positive)
- Add `PUT`, `DELETE`, and `PATCH` APIs
- Add pagination for large datasets
- Protect API with authentication
