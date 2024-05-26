from django.db import models

# Create your models here.
class Parking(models.Model):
    address = models.TextField(max_length = 255)
    duriation = models.CharField(max_length = 20)
    parking_status = models.CharField(max_length = 25)
    parking_number = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    book_date = models.DateField(auto_now_add=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now=True)
    account_bal = models.DecimalField(max_digits=1000000, decimal_places=2, default=20)
