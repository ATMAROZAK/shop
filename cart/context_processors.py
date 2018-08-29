from .cart import Cart
from django.utils.translation import get_language

def cart(request):
    return {'cart': Cart(request)}


def lang(request):
    return {'lang': get_language()}