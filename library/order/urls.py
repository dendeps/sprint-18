from django.urls import path, include
from .views import OrderListView, order_form, OrderDeleteView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('orders', OrderListView.as_view(), name='order-list'),
    path('orders/create', order_form, name='order-create'),
    path("orders/<int:pk>/update", order_form, name="order-update"),
    path("orders/<int:pk>/delete", OrderDeleteView.as_view(), name="order-delete"),
]