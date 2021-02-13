from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Order_info
from .forms import OrderForm

def orderinfo(request):
    context = {
        'orders': Order_info.objects.all()
    }
    return render(request, 'ordersite/order_info_list.html', context)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order_info
    template_name = 'ordersite/order_info_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'orders'
    # ordering = ['-date_posted']

    def get_queryset(self):
        queryset = Order_info.objects.filter(merchant=self.request.user)
        return queryset


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order_info

    def get_queryset(self):
        queryset = Order_info.objects.filter(merchant=self.request.user)
        return queryset


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    template_name = 'ordersite/order_info_form.html'

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
    model = Order_info
    form_class = OrderForm
    template_name = 'ordersite/order_info_form.html'

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.merchant:
            return True
        return False


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order_info
    success_url = '/'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.merchant:
            return True
        return False