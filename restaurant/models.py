from django.db import models
from datetime import date


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_num = models.SmallIntegerField(default=1)
    bookingDate = models.DateField(default=date.today)


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
