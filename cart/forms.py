

from django import forms

from orders.models import ShippingInformation


class ConfirmBookingForm(forms.ModelForm):

    class Meta:
        model = ShippingInformation
        fields = ('name', 'email', 'phone', 'address', 'postal_code', 'city')
