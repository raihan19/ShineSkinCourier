from django import forms
from accounts.models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['amount'].disabled = True
        # super().__init__(*args, **kwargs)
        # self.fields['service_charge'].queryset = Order_price.objects.none()
        self.fields['customer_email'].required = False
        self.fields['product_name'].required = False
        self.fields['product_price'].required = False
        self.fields['product_category'].required = False
        self.fields['product_description'].required = False
        self.fields['delivery_instruction'].required = False
        self.fields['customer_name'].required = True
        self.fields['customer_phone'].required = True
        self.fields['product_weight'].required = True
        self.fields['delivery_address'].required = True
        self.fields['delivery_area'].required = True
        # self.fields['customer_name'].required = True
        # self.fields['customer_name'].required = True
        # self.fields['customer_name'].required = True

        # if 'delivery_option' in self.data:
        #     try:
        #         delivery_option_id = int(self.data.get('delivery_option'))
        #         self.fields['service_charge'].queryset = Order_price.objects.filter(delivery_option_id=delivery_option_id).order_by('service_charge')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     try:
        #         self.fields['service_charge'].queryset = self.instance.delivery_option.service_charge_set.order_by('service_charge')
        #     except:
        #         pass

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['merchant', 'status', 'note', 'received_from_customer',
                   'total_received_or_sent', 'due', 'amount']

