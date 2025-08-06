from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import product

from  .serializers  import ProductSerializer
 
@api_view(['GET'])
def senddata(request):
    all_data = product.objects.all()
    all_data = ProductSerializer(all_data, many =True)
    return Response({"msg":"hello","data":all_data.data})


@api_view(['POST'])
def getdata(request):
    new_pro =request.data
    new_pro = ProductSerializer(data=new_pro)
    if new_pro.is_valid():
        new_pro.save()
        return Response({"msg":"data recived successfully","Data":new_pro.data})
    else:
        return Response({"msg":"Dara Not Recived"})
    
    
    
    
   