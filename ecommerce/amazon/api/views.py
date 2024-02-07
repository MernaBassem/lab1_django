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
 
# @api_view(['GET', 'POST'])
# def AddProduct(request):
#     if request.method == 'POST':
#         serializer = productSerlizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Product added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({'msg': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         return Response({'msg': 'Use POST method to add a product'})


@api_view(['POST'])
def AddProduct(request):
    obj=productSerlizer(data=request.data)
    if(obj.is_valid()):
        obj.save()
        return Response({'msg': 'DONE'})
    return Response({'msg': 'error','error':obj.errors})
