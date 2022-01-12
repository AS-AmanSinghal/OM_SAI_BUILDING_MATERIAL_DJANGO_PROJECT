from django import forms

from .models import Category, SubCategory, Brand


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Category Name'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ('image', 'name')


class SubCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Sub Category Name'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SubCategory
        fields = ('image', 'category', 'name')


class BrandForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        self.fields['brand_name'].widget.attrs['placeholder'] = 'Enter Brand Name'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Brand
        fields = ('image', 'sub_category', 'brand_name')
