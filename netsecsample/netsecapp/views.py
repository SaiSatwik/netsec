# api/views.py
from rest_framework import generics
from .models import DeviceIp
from .serializers import DeviceIpSerializer


class DeviceIpList(generics.ListCreateAPIView):
    queryset = DeviceIp.objects.all()
    serializer_class = DeviceIpSerializer

class DeviceIpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceIp.objects.all()
    serializer_class = DeviceIpSerializer
