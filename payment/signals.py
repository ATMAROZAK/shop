from django.shortcuts import get_object_or_404

from orders.models import Order


"""def PaymentNotification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()

valid_ipn_received.connect(PaymentNotification)"""