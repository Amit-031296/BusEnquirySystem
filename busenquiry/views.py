from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

# Create your views here.

class TransportCompanyListCreate(ListCreateAPIView):
    serializer_class = TransportCompanySerializer

    def get_queryset(self):
        queryset = TransportCompany.objects.all().order_by('-id')
        return queryset

class TransposrtCompanyRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class BusListCreate(ListCreateAPIView):
    serializer_class = BusSerializer

    def get_queryset(self):
        queryset = Bus.objects.all().order_by('-id')
        return queryset

class BusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [permissions.IsAuthenticated]

class StopsListCreate(ListCreateAPIView):
    serializer_class = StopsSerializer

    def get_queryset(self):
        queryset = Stops.objects.all().order_by('-id')
        return queryset

class StopsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer
    permission_classes = [permissions.IsAuthenticated]

class RoutesListCreate(ListCreateAPIView):
    serializer_class = RoutesSerializer

    def get_queryset(self):
        queryset = Routes.objects.all().order_by('-id')
        return queryset

class RoutesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScheduleListCreate(ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all().order_by('-id')
        return queryset

class ScheduleRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]