from django.db import models


class DeviceIp(models.Model):
    device_name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return self.device_name
