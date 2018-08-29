from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('<slug:category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<int:id>/<slug:slug>/', views.ProductDetail, name='ProductDetail'),
    path('', views.ProductList, name='ProductList')

]

