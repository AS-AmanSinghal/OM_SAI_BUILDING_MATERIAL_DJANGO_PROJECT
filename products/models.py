import os.path
import sys
import uuid
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from category.models import SubCategory, Brand


# Create your models here.


class Product(models.Model):
    STATUS = [
        (True, 'In Stock'),
        (False, 'Out of Stock')
    ]

    def get_upload_path(instance, filename):
        return os.path.join("products", "%s" % instance.name, filename)

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=15, null=False, blank=False)
    mrp = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=10000)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=get_upload_path)
    description = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        # opening Image
        im = Image.open(self.image)
        output = BytesIO()
        # resize the modify
        im = im.resize((1024, 720))
        # after modification save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)
        # change imagefield value to the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % uuid.uuid4(), 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Product, self).save()

    @receiver(pre_save)
    def before_save_model(sender, instance, **kwargs):
        try:
            if instance.stock > 0:
                instance.status = True
            else:
                instance.status = False
            instance.discount = ((instance.mrp - instance.price) / instance.mrp) * 100
        except Exception as e:
            pass

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Images(models.Model):
    def get_upload_path(instance, filename):
        return os.path.join("products/images/", "%s" % instance.product.name, filename)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        # opening Image
        im = Image.open(self.image)
        output = BytesIO()
        # resize the modify
        im = im.resize((1024, 720))
        # after modification save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)
        # change imagefield value to the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % uuid.uuid4(), 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Images, self).save()

    def __str__(self):
        return f'{self.product.name}'
