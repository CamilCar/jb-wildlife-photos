

from django import forms

from orders.models import ShippingInformation


class ConfirmBookingForm(forms.ModelForm):
    """
    Creates the form for shipping information for
    checkout page
    """
    class Meta:
        model = ShippingInformation
        fields = ('name', 'email', 'phone', 'address', 'postal_code', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name',
                                                 'class': 'form-control col-xs-3'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email',
                                                  'class': 'form-control col-xs-3'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone',
                                                  'class': 'form-control col-xs-3'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Address',
                                                    'class': 'form-control col-xs-3'})
        self.fields['postal_code'].widget.attrs.update({'placeholder': 'Postal_code',
                                                        'class': 'form-control col-xs-3'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City',
                                                 'class': 'form-control col-xs-3'})
