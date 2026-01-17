from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TestDrive(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    preferred_date = models.DateField(default=timezone.now)
    preferred_time = models.TimeField(default=timezone.now)


class CarConfiguration(models.Model):
    CAR_CHOICES = [
        ('LS6', 'LS6'),
        ('LS8', 'LS8'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    car_model = models.CharField(max_length=10, choices=CAR_CHOICES)
    package = models.CharField(max_length=50)
    exterior = models.CharField(max_length=50)
    interior = models.CharField(max_length=50)
    saved_at = models.DateTimeField(default=timezone.now)
