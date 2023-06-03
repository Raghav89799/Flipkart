from rest_framework import serializers
from customer.models import *

class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class GetCustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__" 


class GetCustomerDetailsAddressSerializer(serializers.ModelSerializer):
    
    customer_addresses = GetCustomerSerializer(many=True)
    class Meta:
        model = Customer
        fields = ('first_name','last_name','mobile','age','country','city','dob')


