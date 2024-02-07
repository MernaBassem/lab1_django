from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from amazon.models import *
from .serizer import *
 

@api_view(['GET'])
def Hello(request):
    return Response({'msg':'hello Merna'})

@api_view(['GET','POST'])
def AcceptData(request):
    print(request.method) #method
    print(request.data) #data
    return Response({'msg':'ACCEPT DATA','data':request.data})

@api_view(['GET'])
def all(request) :
    data = Product.objects.all()
    datajson=productSerlizer(data,many=True).data
    return Response({'msg':'ACCEPT DATA','data':datajson})


@api_view(['GET'])
def getProduct(request,id) :
    datajson=productSerlizer( Product.get_product_detail(id)).data
    return Response({'msg':'ACCEPT DATA','data':datajson})
 

@api_view(['POST'])
def AddProduct(request):
    obj=productSerlizer(data=request.data)
    if(obj.is_valid()):
        obj.save()
        return Response({'msg': 'DONE'})
    return Response({'msg': 'error','error':obj.errors})


@api_view(['PUT'])
def UpdateProduct(request, id):
    updateProduct = Product.objects.filter(id=id).first()
    if updateProduct:
        product = productSerlizer(instance=updateProduct, data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data)
    return Response({'msg': ''})
