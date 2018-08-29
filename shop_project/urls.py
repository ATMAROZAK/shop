from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


#urlpatterns = i18n_patterns(
urlpatterns = [
    path('admin/', admin.site.urls),
    path('^i18n/', include('django.conf.urls.i18n')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('order/', include(('orders.urls', 'orders'), namespace='orders')),

    #path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('', include(('product_app.urls', 'product_app'), namespace='product_app')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
