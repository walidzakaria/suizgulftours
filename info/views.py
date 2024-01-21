from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, views
from rest_framework.response import Response
from django.http import QueryDict
import random

from .serializers import GuestInfoSerializer, HotelSerializer, NationalitySerializer
from .models import Tblguestinfo, Tblhotel, Tblnationality
from .utils import create_id


@api_view(['GET'])
def list_hotels(request):
    if request.method == 'GET':
        hotels = Tblhotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_nationalities(request):
    if request.method == 'GET':
        nationality = Tblnationality.objects.all()
        serializer = NationalitySerializer(nationality, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_registration(request, request_id):
    if request.method == 'GET':
        registration = Tblguestinfo.objects.filter(guestinfoid=request_id).first()
        if not registration:
            return Response(data={'error': 'no data'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GuestInfoSerializer(registration)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_registration(request):
    if request.method == 'POST':        
        registration_data = request.data.copy()
        registration_data['guestinfoid'] = create_id()
        serializer = GuestInfoSerializer(data=registration_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_registration(request, request_id):
    if request.method == 'PUT':
        registration = Tblguestinfo.objects.filter(guestinfoid=request_id).first()
        if not registration:
            return Response(data={'error': 'no data'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GuestInfoSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
