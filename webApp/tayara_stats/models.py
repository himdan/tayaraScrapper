from django.db import models


class Media(models.Model):
    href = models.CharField(max_length=100, unique=True)


class Location(models.Model):
    delegation = models.CharField(max_length=100)
    governorate = models.CharField(max_length=100)


class Publisher(models.Model):
    isApproved = models.BooleanField()
    name = models.CharField(max_length=100)
    isShop = models.BooleanField()
    avatar = models.CharField(max_length=100)


class RealEstate(models.Model):
    reference = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=100)
    imgLoad = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    phone = models.CharField(max_length=100)
    """Metadata"""
    publishedOn = models.DateTimeField()
    isModified = models.BooleanField()
    subCategory = models.CharField(max_length=30)
    isFeatured = models.BooleanField()
    producttype = models.IntegerField()
    """"""
    images = models.ManyToManyField(Media)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
