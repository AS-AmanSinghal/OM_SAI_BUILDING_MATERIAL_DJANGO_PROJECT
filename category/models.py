import sys
import uuid
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


# Create your models here.


class Category(models.Model):

    image = models.ImageField(upload_to='product/category')
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        # opening Image
        im = Image.open(self.image)
        output = BytesIO()
        # resize the modify
        im = im.resize((720, 360))
        # after modification save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)
        # change imagefield value to the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % uuid.uuid4(), 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Category, self).save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class SubCategory(models.Model):

    image = models.ImageField(upload_to='product/sub_category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        # opening Image
        im = Image.open(self.image)
        output = BytesIO()
        # resize the modify
        im = im.resize((720, 360))
        # after modification save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)
        # change imagefield value to the newly modified image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % uuid.uuid4(), 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(SubCategory, self).save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'


class Brand(models.Model):
    image = models.ImageField(upload_to='product/sub_category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=15, null=False, blank=False)
    status = models.BooleanField(default=True)
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
        super(Brand, self).save()

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
