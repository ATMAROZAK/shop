from decimal import Decimal
from django.conf import settings
from product_app.models import Product, Price
from django.shortcuts import render, get_object_or_404


class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    #Добавление товара либо обновление количества
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price_rub = get_object_or_404(Price, currency__name='RUB', product__id=product_id).value
        price_usd = get_object_or_404(Price, currency__name='USD', product__id=product_id).value

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price_rub': str(price_rub),
                                     'price_usd': str(price_usd)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():

            item['price_rub'] = Decimal(item['price_rub'])
            item['total_price_rub'] = item['price_rub'] * item['quantity']

            item['price_usd'] = Decimal(item['price_usd'])
            item['total_price_usd'] = item['price_usd'] * item['quantity']
            yield item

    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price_rub(self):
        return sum(Decimal(item['price_rub']) * item['quantity'] for item in self.cart.values())

    def get_total_price_usd(self):
        return sum(Decimal(item['price_usd']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True