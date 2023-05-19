from django.db import models


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
    images = models.JSONField()
    """Publisher"""
    pub_isApproved = models.BooleanField()
    pub_name = models.CharField(max_length=100)
    pub_isShop = models.BooleanField()
    pub_avatar = models.CharField(max_length=100)
    """location"""
    loc_delegation = models.CharField(max_length=100)
    loc_governorate = models.CharField(max_length=100)
