from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class People(models.Model):
    basic_info = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="people_info"
    )
    image_url = models.URLField()
    phone_no = models.CharField(max_length=12)
    active_status = models.BooleanField(default=False)  # type: ignore
    balance = models.DecimalField(decimal_places=2, default_value=0.00, max_digits=12)
