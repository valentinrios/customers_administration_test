# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Customer
from .models import Country
from .models import Sport
from .serializers import CustomerSerializer
from .serializers import CountrySerializer
from .serializers import SportSerializer

class CustomerList(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer =  CustomerSerializer(customers, many = True)
        return Response(serializer.data)

class CustomerDetails(APIView):

	def get(self, request, pk):
		customer = Customer.objects.get(pk=pk)
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)

	def put(self, request):
		serializer = CustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		Customer.objects.filter(id=request.data['id']).update(name=request.data['name'])
		return Response(status=status.HTTP_202_ACCEPTED)

	def delete(self, request, pk):
		customer = Customer.objects.get(pk=pk)
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CountryList(APIView):

    def get(self, request):
        countries = Country.objects.all()
        serializer =  CountrySerializer(countries, many = True)
        return Response(serializer.data)

class CountryDetails(APIView):

	def get(self, request, pk):
		country = Country.objects.get(pk=pk)
		serializer = CountrySerializer(country)
		return Response(serializer.data)

	def put(self, request):
		serializer = CountrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		country = Country.objects.get(pk=pk)
		country.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SportList(APIView):

    def get(self, request):
        sports = Sport.objects.all()
        serializer =  SportSerializer(sports, many = True)
        return Response(serializer.data)

class SportDetails(APIView):

	def get(self, request, pk):
		sport = Sport.objects.get(pk=pk)
		serializer = SportSerializer(sport)
		return Response(serializer.data)

	def put(self, request):
		serializer = SportSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		sport = Sport.objects.get(pk=pk)
		sport.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)