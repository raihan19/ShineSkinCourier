from django import forms
from .models import Order_info


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['service_charge'].disabled = True

    class Meta:
        model = Order_info
        fields = ['first_name', 'last_name', 'delivery_address', 'contact_no',
              'delivery_instruction', 'delivery_option', 'service_charge',
              'delivery_area']