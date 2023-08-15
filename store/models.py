from django.db import models
from django.contrib.auth.models import User
from .validators import filesize
import os
from userprofile.models import Vendor
from django.db.models.signals import pre_delete
from django.dispatch import receiver
class Category(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.tittle
class Product(models.Model):
    ACTIVE = 'active'
    DELETED = 'deleted'
    STATUS_CHOICES = (
        (ACTIVE,"active"),
        (DELETED,"deleted")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True)
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    video = models.FileField(upload_to="media/productvideo",validators=[filesize],null=True)
    banner = models.ImageField(upload_to=("bannerimage"),null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default=ACTIVE)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only multiply price during creation
            self.price *= 100
        super(Product, self).save(*args, **kwargs)
    def pricedisplay(self):
        return self.price / 100 
    @receiver(pre_delete, sender=User)
    def delete_user_products(sender, instance, **kwargs):
        if instance.products.exists():
            instance.products.all().delete()
    @receiver(pre_delete, sender=Vendor)
    def delete_vendor_products(sender, instance, **kwargs):
        instance.user.products.all().delete()
    def delete(self, *args, **kwargs):
        # Delete associated media files before deleting the instance
        if self.video:
            if os.path.exists(self.video.path):
                os.remove(self.video.path)
        if self.banner:
            if os.path.exists(self.banner.path):
                os.remove(self.banner.path)
        super(Product, self).delete(*args, **kwargs)