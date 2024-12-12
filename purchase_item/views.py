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
        # Emailing Confirmations
        # send_email.success_email(
        #     request=request,
        #     subject="Puchased Items successfully",
        #     message="Great, You've puchased these",
        #     success_url="/",
        #     # Need to UPDATE
        #     domain="/",
        # )
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
