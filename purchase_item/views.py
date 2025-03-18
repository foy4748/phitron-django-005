import uuid

# from rest_framework.fields import timezone
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from cart_item.models import CartItem
from purchase_item.models import PurchasedItem
from purchase_item.serializers import PurchasedItemSerializer
from transaction.constants import PURCHASE
from transaction.models import Transaction
from utils import send_email

from project.settings import FRONTEND_LINK

import environ
from sslcommerz_lib import SSLCOMMERZ

# reading .env file
env = environ.Env()
environ.Env.read_env()

## Create your views here.


# Creating Payment Intent of items in the cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def CreatePaymentIntent(request):
    cart_items = CartItem.objects.filter(cart_item_owner=request.user)
    # purchased_items = list()
    current_total = 0
    for item in cart_items:
        current_total = current_total + float(item.quantity) * float(
            item.product.unit_price
        )

    # if current_total <= float(request.user.people_info.balance):
    transaction_id = uuid.uuid4()  # Generates a random UUID
    print(transaction_id)
    payment_intent = createPaymentIntent(
        current_total, transaction_id=transaction_id, user_email=request.user.email
    )
    return Response(payment_intent)
    # else:
    #     return Response(
    #         {
    #             "success": False,
    #             "message": "Product(s) Purchase FAILED. Insufficient Balance",
    #         }
    #     )


# Performing Purchase operation of items in the cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@transaction.atomic
def PurchaseItemView(request, transaction_id):
    cart_items = CartItem.objects.filter(cart_item_owner=request.user)
    purchased_items = list()
    current_total = 0
    for item in cart_items:
        current_total = current_total + float(item.quantity) * float(
            item.product.unit_price
        )

    # if current_total <= float(request.user.people_info.balance):
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
        single_transaction = Transaction(
            type=PURCHASE,
            purchased_product=single_purchased_item,
            amount=float(item.quantity) * float(item.product.unit_price),
            transaction_id=transaction_id,
            buyer=request.user,
            seller=item.product.product_owner,
        )
        single_transaction.save()
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
    # else:
    #     return Response(
    #         {
    #             "success": False,
    #             "message": "Product(s) Purchase FAILED. Insufficient Balance",
    #         }
    #     )


# Payment Related


def createPaymentIntent(
    amount,
    transaction_id,
    user_email,
    success_url=None,
    user_phone="",
    user_address="",
    user_city="",
    user_country="",
):
    # Payment Related
    payment_settings = {
        "store_id": env("SSLCOMMERZ_STORE_KEY"),
        "store_pass": env("SSLCOMMERZ_STORE_PASS"),
        "issandbox": True,
    }
    sslcz = SSLCOMMERZ(payment_settings)
    post_body = {}

    if success_url is None:
        post_body[
            "success_url"
        ] = f"{FRONTEND_LINK}/api/payment-success/{transaction_id}"
    else:
        post_body["success_url"] = success_url

    post_body["total_amount"] = amount
    post_body["currency"] = "BDT"
    post_body["tran_id"] = transaction_id
    post_body["cus_email"] = user_email
    # post_body["success_url"] = f"{FRONTEND_LINK}"
    post_body["fail_url"] = f"{FRONTEND_LINK}/api/payment-failed/{transaction_id}"
    post_body["cus_phone"] = "017000000000"
    post_body["cus_add1"] = user_address
    post_body["cus_city"] = user_city
    post_body["cus_country"] = user_country
    post_body["shipping_method"] = "NO"
    post_body["product_name"] = transaction_id
    post_body["product_category"] = transaction_id
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
