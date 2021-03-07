from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from accounts.models import Order
from .forms import OrderForm

# def load_prices(request):
#     delivery_option_id = request.GET.get('delivery_option')
#     prices = Order_price.objects.filter(delivery_option_id=delivery_option_id).order_by('service_charge')
#     return render(request, 'ordersite/price_dropdown_list_options.html', {'prices': prices})

def orderinfo(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'ordersite/order_list.html', context)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'ordersite/order_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'orders'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        queryset = Order.objects.filter(merchant=self.request.user)
        return queryset


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

    def get_queryset(self):
        queryset = Order.objects.filter(merchant=self.request.user)
        return queryset


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    template_name = 'ordersite/order_form.html'

    # def get_initial(self):
    #     order = get_object_or_404(Order_info, pk=self.kwargs['order_info_id'])
    #     self.initial.update({
    #         'merchant': self.request.user.id,
    #         'service_charge': order.service_charge,
    #     })
    #     return super(OrderCreateView, self).get_initial()


    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'ordersite/order_form.html'

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.merchant:
            return True
        return False


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.merchant:
            return True
        return False