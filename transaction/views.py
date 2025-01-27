from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def FailedTransaction(request, transaction_id):
    return Response(
        {
            "success": False,
            "message": f"Failed Transaction {transaction_id}",
        }
    )
