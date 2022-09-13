from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView

from .forms import OrderForm
from .models import Order
from authentication.models import CustomUser
from book.models import Book


class OrderListView(ListView):
    model = Order
    template_name = 'user/order_list.html'
    context_object_name = 'items'


def order_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=pk)
            form = OrderForm(instance=order)
        return render(request, 'order/order_form.html', {'form': form})
    else:
        if pk == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=pk)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

            '''user_id = int(request.POST.get('user'))
            user = CustomUser.get_by_id(user_id)
            book_id = int(request.POST.get('book'))
            book = Book.get_by_id(book_id)
            plated_end_at = request.POST.get('plated_end_at')
            order = Order.create(user, book, plated_end_at)
            
            if order is not None:
                return redirect('/orders')
            else:
                context = {
                    'message': f'Order was not created'
                }
                return render(request, 'order/error.html', context)'''
        return redirect('/orders')


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/orders"
    template_name = "order/delete_order.html"
