from rest_framework import serializers
from .models import Customer
from .models import Country
from .models import Sport

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        #fields = ('name','type_field','metric')
        fields = '__all__'
    
class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        #fields = ('name','type_field','metric')
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        #fields = ('name','type_field','metric')
        fields = '__all__'
