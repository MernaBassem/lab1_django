from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
    