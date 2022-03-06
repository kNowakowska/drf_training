from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from passengerApp.models import Passenger
from passengerApp.serializers import PassengerSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        passengers_serializer = PassengerSerializer(passengers, many=True)
        return Response(passengers_serializer.data)
    elif request.method == 'POST':
        passenger_serializer = PassengerSerializer(data=request.data)
        if passenger_serializer.is_valid():
            passenger_serializer.save()
            return Response(passenger_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail(request, id):
    try:
        passenger = Passenger.objects.get(pk=id)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        passenger_serializer = PassengerSerializer(passenger)
        return Response(passenger_serializer.data)
    elif request.method == 'PUT':
        passenger_serializer = PassengerSerializer(passenger, data=request.data)
        if passenger_serializer.is_valid():
            passenger_serializer.save()
            return Response(passenger_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
