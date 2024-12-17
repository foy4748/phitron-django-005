# Create your views here.
# views.py
from django.shortcuts import render

from purchase_item.models import PurchasedItem
from purchase_item.serializers import PurchasedItemSerializer


def product_purchase_email_preview(request):
    _purchase_history = PurchasedItem.objects.all()
    purchase_history = PurchasedItemSerializer(_purchase_history, many=True)
    context = {
        "message": "TEST MESSAGE",
        "username": "test",
        "domain": "http://localhost:3001",
        "success_url": "/auth/activate/test/test/",
        "purchase_history": purchase_history.data,
    }
    return render(request, "product_purchase.html", context)
