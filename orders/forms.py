from django import forms

from .models import Wishlist, Cart, OrderItem


class DeleteWishlistForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeleteWishlistForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Wishlist
        fields = ['user']


class DeleteCartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteCartForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Cart
        fields = ['user']


class OrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label != 'Status':
                field.disabled = True
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = OrderItem
        fields = ['product_name', 'price', 'discount', 'quantity', 'status']
