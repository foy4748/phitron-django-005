# Create your views here.
# views.py
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from purchase_item.models import PurchasedItem
from purchase_item.serializers import PurchasedItemSerializer
from purchase_item.views import createPaymentIntent


def product_purchase_email_preview(request):
    _purchase_history = PurchasedItem.objects.all()
    purchase_history = PurchasedItemSerializer(_purchase_history, many=True)
    context = {
        "message": "You've successfully purchased these",
        "username": "test",
        "domain": "https://phitron-sdt-assignment-05-frontend.vercel.app",
        "success_url": "/auth/activate/test/test/",
        "purchase_history": purchase_history.data,
    }
    return render(request, "product_purchase.html", context)


def account_activation_email_preview(request):
    context = {
        "message": "Click the button below to activate your account",
        "username": "test",
        "domain": "https://phitron-sdt-assignment-05-frontend.vercel.app",
        "success_url": "/activate/test/test/",
    }
    return render(request, "account_activation_email.html", context)


class PaymentTesting(APIView):
    def get(self, request):
        res = createPaymentIntent()
        return Response(res)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def test_protected_route(_):
    return Response({"success": True, "message": "User is authenticated"})
