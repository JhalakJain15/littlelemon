from django.db import models
class Menu(models.Model):
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.date_time}"

# Create your models here.
