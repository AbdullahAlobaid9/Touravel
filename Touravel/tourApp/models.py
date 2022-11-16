from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):

    city_type_choices = models.TextChoices("City type", ["Riyadh", "Hail", "Al Ula"])

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    place_name = models.CharField(max_length= 1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    city = models.CharField(max_length=64, choices= city_type_choices.choices, default=city_type_choices.Riyadh)   

    def __str__(self) -> str:
        return f"{self.place_name}, {self.city}"

class Review(models.Model):

    place = models.ForeignKey(Place, on_delete= models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} , {self.content}"


class Reservation(models.Model):
    
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    place = models.ForeignKey(Place, on_delete= models.CASCADE)

    book_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user},{self.place},{self.book_date}"

