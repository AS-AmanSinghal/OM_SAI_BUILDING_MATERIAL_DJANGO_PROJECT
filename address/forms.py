from django import forms

from .models import ShippingCharges


class ShippingChargeForm(forms.ModelForm):
    class Meta:
        model = ShippingCharges
        fields = ['pincode', 'charges']

    def __init__(self, *args, **kwargs):
        super(ShippingChargeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
