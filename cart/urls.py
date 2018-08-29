from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('remove/<int:product_id>/', views.CartRemove, name='CartRemove'),
    path('add/<int:product_id>/', views.CartAdd, name='CartAdd'),
    path('clear/', views.CartClear, name='CartClear'),
    path('', views.CartDetail, name='CartDetail')
]