from django.urls import path

from transaction.views import FailedTransaction  # ,include

urlpatterns = [
    # Review urls
    path(
        "failed-transaction/<str:transaction_id>/",
        FailedTransaction,
        name="failed_transaction",
    ),
]
