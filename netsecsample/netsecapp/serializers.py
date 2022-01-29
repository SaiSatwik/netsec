from rest_framework import serializers
from .models import DeviceIp


class DeviceIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceIp
        fields = ('device_name', 'ip_address')
