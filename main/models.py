from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Device(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    device_id=models.CharField(max_length=100)
    manual_mode=models.BooleanField(default=False)
    moisture_level=ArrayField(
            models.FloatField(),
            blank=True,
    )
    temperature=ArrayField(
            models.FloatField(),
            blank=True,
    )
    humidity=ArrayField(
            models.FloatField(),
            blank=True,
    )

    def __str__(self) -> str:
        return self.device_id