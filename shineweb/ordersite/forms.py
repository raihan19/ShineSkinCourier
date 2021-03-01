from django import forms
from accounts.models import Order, Order_price


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['service_charge'].disabled = True
        # super().__init__(*args, **kwargs)
        self.fields['service_charge'].queryset = Order_price.objects.none()

        if 'delivery_option' in self.data:
            try:
                delivery_option_id = int(self.data.get('delivery_option'))
                self.fields['service_charge'].queryset = Order_price.objects.filter(delivery_option_id=delivery_option_id).order_by('service_charge')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            try:
                self.fields['service_charge'].queryset = self.instance.delivery_option.service_charge_set.order_by('service_charge')
            except:
                pass

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['merchant']
