from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    registered_on = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.first_name


class Listing(models.Model):
    class SaleType(models.TextChoices):
        PICK_UP = "Available for pickup"
        SHIP = "Available for shipping"
        EITHER = "Ship or Pickup"

    class ConditionType(models.TextChoices):
        USED = "Used"
        NEW = "New"

    class ProductType(models.TextChoices):
        PRINTER = "Printer"
        PARTS = "Parts"
        MODELS = "Models"
        OTHER = "Other"
    customer = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    condition = models.CharField(
        max_length=50, choices=ConditionType.choices, default=ConditionType.USED)
    product_type = models.CharField(
        max_length=50, choices=ProductType.choices, default=ProductType.PRINTER)
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.SHIP)
    price = models.FloatField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    main_photo = models.ImageField(max_length=100)
    photo_1 = models.ImageField(max_length=100)
    photo_2 = models.ImageField(max_length=100, blank=True)
    photo_3 = models.ImageField(blank=True)
    photo_4 = models.ImageField(blank=True)
    list_date = models.DateTimeField(default=now, blank=True)
    contact_email = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'listings'

    def __str__(self):
        return self.title
