# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from product_app.models import Product

class ProductTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Product
    """

    fields = ('description',)

translator.register(Product, ProductTranslationOptions)