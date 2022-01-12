from django import forms

from .models import Product, Images


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'sub_category', 'brand', 'name', 'mrp', 'price', 'stock', 'description')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = 'Enter ' + field.label


class UploadImagesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UploadImagesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Images
        fields = ['image']
