import django_filters
from .models import Order
from django_filters import DateFilter, CharFilter


class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte', label='Start date')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte', label='End date')
	note = CharFilter(field_name='note', lookup_expr='icontains', label='Note')

	class Meta:
		model = Order
		fields = ['merchant__username', 'status', 'id', 'delivery_area']
