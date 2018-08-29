from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.utils.translation import get_language
from .tasks import OrderCreated
from django.shortcuts import render, redirect
from django.urls import reverse


def OrderCreate(request):
    cart = Cart(request)

    if request.method == 'POST':

        form = OrderCreateForm(request.POST)


        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price_rub=item['price_rub'],
                                         price_usd=item['price_usd'],
                                         quantity=item['quantity'])
            if get_language() == 'ru':
                currency = 'RUB'
                total_cost = order.get_total_cost_rub()

            else:
                currency = 'USD'
                total_cost = order.get_total_cost_usd()

            order.currency = currency
            order.total_cost = total_cost
            order.save()
            cart.clear()
            OrderCreated.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))

            #return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})