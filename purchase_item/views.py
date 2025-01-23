from rest_framework.fields import timezone
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from cart_item.models import CartItem
from purchase_item.models import PurchasedItem
from purchase_item.serializers import PurchasedItemSerializer
from utils import send_email

import environ
from sslcommerz_lib import SSLCOMMERZ

# reading .env file
env = environ.Env()
environ.Env.read_env()

## Create your views here.


# Performing Purchase operation of items in the cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@transaction.atomic
def PurchaseItemView(request):
    cart_items = CartItem.objects.filter(cart_item_owner=request.user)
    purchased_items = list()
    current_total = 0
    for item in cart_items:
        current_total = current_total + float(item.quantity) * float(
            item.product.unit_price
        )

    if current_total <= float(request.user.people_info.balance):
        for item in cart_items:
            single_purchased_item = PurchasedItem(
                purchased_item_owner=request.user,
                product=item.product,
                unit_price=item.product.unit_price,
                unit_name=item.product.unit_name,
                quantity=item.quantity,
            )
            item.delete()
            single_purchased_item.save()
            purchased_items.append(single_purchased_item)

        s = PurchasedItemSerializer(purchased_items, many=True)

        # Sending confirmation Email
        send_email.purchase_confirmation_email(
            user_email=request.user.email,
            subject="Puchased Items successfully",
            message="Puchase Items were Successful",
            success_url="/dashboard/user/purchase-history",
            domain="https://phitron-sdt-assignment-05-frontend.vercel.app",
            purchase_history=s.data,
        )
        return Response(
            {
                "success": True,
                "message": "Product(s) Purchased Successfully",
                "purchased_items": s.data,
            }
        )
    else:
        return Response(
            {
                "success": False,
                "message": "Product(s) Purchase FAILED. Insufficient Balance",
            }
        )


# Payment Related


def createPaymentIntent():
    # Payment Related
    payment_settings = {
        "store_id": env("SSLCOMMERZ_STORE_KEY"),
        "store_pass": env("SSLCOMMERZ_STORE_PASS"),
        "issandbox": True,
    }
    print(payment_settings)
    sslcz = SSLCOMMERZ(payment_settings)
    post_body = {}
    post_body["total_amount"] = 100.26
    post_body["currency"] = "BDT"
    post_body["tran_id"] = "12345"
    post_body["cus_email"] = "faisaljfcl@gmail.com"
    post_body["success_url"] = "http://localhost:3001"
    post_body["cus_phone"] = "01700000000"
    post_body["cus_add1"] = "customer address"
    post_body["cus_city"] = "Dhaka"
    post_body["cus_country"] = "Bangladesh"
    post_body["shipping_method"] = "NO"
    post_body["product_name"] = "Test"
    post_body["product_category"] = "Test Category"
    post_body["product_profile"] = "general"
    payment_intent = sslcz.createSession(post_body)
    # END OF Payment Related ----------
    # print(payment_intent)
    return payment_intent


# User specific Purchased Item List
class PurchasedItemListView(ListAPIView):
    serializer_class = PurchasedItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        data = PurchasedItem.objects.filter(purchased_item_owner=self.request.user)
        return data
