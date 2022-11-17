from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GuideProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to="images/", default="images/tourist.png")
    national_id = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user}, {self.national_id}"
