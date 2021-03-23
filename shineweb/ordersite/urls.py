from django.urls import path
from .views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderTransactionListView,
    OrderTransactionHistoryDetailView,
    # load_prices
)

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('order/<str:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('ordercreate/new/', OrderCreateView.as_view(), name='order-create'),
    path('order/<str:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<str:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('ordertransaction/', OrderTransactionListView.as_view(), name='order-transaction-list'),
    path('ordertransaction/detail/<str:pk>/', OrderTransactionHistoryDetailView.as_view(), name='order-transaction-detail'),
    # path('ajax/load-prices/', load_prices, name='ajax_load_prices'),
]