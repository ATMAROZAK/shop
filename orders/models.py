from django.db import models
from product_app.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address =  models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(verbose_name='Почтовый код', max_length=20)
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    total_cost = models.DecimalField(verbose_name='Итого', max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(verbose_name='Валюта', max_length=3)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost_rub(self):
        return sum(item.get_cost_rub() for item in self.items.all())

    def get_total_cost_usd(self):
        return sum(item.get_cost_usd() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price_rub = models.DecimalField(verbose_name='Цена руб', max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(verbose_name='Цена usd', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost_rub(self):
        return self.price_rub * self.quantity

    def get_cost_usd(self):
        return self.price_usd * self.quantity