from django.db import models

# Create your models here.

from django.db import models
# Create your models here.
TYPES = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna")
)
class Category(models.Model):
    name = models.CharField(max_length=64)
class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    type = models.IntegerField(choices=TYPES, default="fundacja")
    categories = models.ManyToManyField(Category)
class Donation(models.Model):
    quantity = models.FloatField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.ForeignKey('StreetAddress', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.CharField(max_length=256)
class StreetAddress(models.Model):
    text = models.TextField()
    line_number = models.IntegerField()