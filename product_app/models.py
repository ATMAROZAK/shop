from django.db import models
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_app:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', verbose_name="Категория", null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    #price_rub = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена RUB")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_price(self):
        lang = get_language()

        if lang == 'ru':
            price = get_object_or_404(Price, currency__name="RUB", product__id=self.id)
        else:
            price = get_object_or_404(Price, currency__name="USD", product__id=self.id)

        print(lang)
        return price

    def get_absolute_url(self):
        return reverse('product_app:ProductDetail', args=[self.id, self.slug])

class Currency(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название валюты", unique=True)
    symbol = models.CharField(max_length=1, verbose_name="Символ")

    class Meta:
        ordering = ['name']
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Валюта")
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")

    class Meta:
        ordering = ['product']
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.product.name