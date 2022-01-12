from django.db import models


# Create your models here.


class Category(models.Model):
    STATUS = [
        (True, 'Active'),
        (False, 'InActive')
    ]
    image = models.ImageField(upload_to='product/category')
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    status = models.BooleanField(choices=STATUS, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class SubCategory(models.Model):
    STATUS = [
        (True, 'Active'),
        (False, 'InActive')
    ]
    image = models.ImageField(upload_to='product/sub_category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    status = models.BooleanField(choices=STATUS, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'


class Brand(models.Model):
    STATUS = [
        (True, 'Active'),
        (False, 'InActive')
    ]
    image = models.ImageField(upload_to='product/sub_category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=15, null=False, blank=False)
    status = models.BooleanField(choices=STATUS, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
