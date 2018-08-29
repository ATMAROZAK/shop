from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Price
from cart.forms import CartAddProductForm

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    lang = get_language()
    if lang is 'ru':
        price = get_object_or_404(Price, currency__name="RUB", product=product)
    else:
        price = get_object_or_404(Price, currency__name="USD", product=product)

    cart_product_form = CartAddProductForm()


    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'price' : price,
                   'cart_product_form': cart_product_form
                   })


def index(request):
    msg = _("Milk")
    return render(request, 'index.html', {'message' : msg})



