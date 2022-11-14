from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    profile_picture = models.ImageField()
    national_id = models.IntegerField()
    phone_number = models.IntegerField()
