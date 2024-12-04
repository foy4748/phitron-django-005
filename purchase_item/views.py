from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from cart_item.models import CartItem
from cart_item.serializers import CartItemSerializer
from purchase_item.models import PurchasedItem


# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@transaction.atomic
def PurchaseItemView(request):
    cart_items = CartItem.objects.filter(cart_item_owner=request.user)
    s = CartItemSerializer(cart_items, many=True)
    for item in cart_items:
        purchase_item = PurchasedItem(
            purchased_item_owner=request.user,
            product=item.product,
            unit_price=item.product.unit_price,
            unit_name=item.product.unit_name,
            quantity=item.quantity,
        )
        print(purchase_item)
        # purchase_item.save()

    return Response(
        {"success": True, "message": "Product Purchased Successfully", "s": s.data}
    )
