from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import *
from customer.serializers import *

# Create your views here.

class GetCustomerView(APIView):

    def get(self,request):
        instance = Customer.objects.all()
        ser = GetCustomerSerializer(instance,many=True)
        return Response(ser.data)
    
    def post(self,request):
        params = request.data
        print("Data",params)
        ser = GetCustomerSerializer(data = params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"Message":"Save Successfully"})
    

class GetCustomerAddressView(APIView):
    
    def get(self,request):
        instance = CustomerAddress.objects.all()
        ser = GetCustomerAddressSerializer(instance,many=True)
        return Response(ser.data)
    

class GetCustomerDetailAddressView(APIView):

    def get(self,request,pk):
        instances = Customer.objects.filter(id=pk)
        ser = GetCustomerDetailsAddressSerializer(instances,many=True)
        return Response(ser.data)


    

    
    

 