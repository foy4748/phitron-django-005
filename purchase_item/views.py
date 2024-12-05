from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from cart_item.models import CartItem
from cart_item.serializers import CartItemSerializer
from purchase_item.models import PurchasedItem
from purchase_item.serializers import PurchasedItemSerializer


## Create your views here.


# Performing Purchase operation of items in the cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@transaction.atomic
def PurchaseItemView(request):
    cart_items = CartItem.objects.filter(cart_item_owner=request.user)
    purchased_items = list()
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
    return Response(
        {
            "success": True,
            "message": "Product(s) Purchased Successfully",
            "purchased_items": s.data,
        }
    )


# User specific Purchased Item List
class PurchasedItemListView(ListAPIView):
    serializer_class = PurchasedItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        data = PurchasedItem.objects.filter(purchased_item_owner=self.request.user)
        return data
