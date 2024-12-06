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
    balance = models.DecimalField(decimal_places=2, default=0.00, max_digits=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.basic_info.username}"
