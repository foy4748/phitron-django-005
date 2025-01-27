from django.urls import path

from transaction.views import FailedTransaction  # ,include

urlpatterns = [
    # Review urls
    path("failed-transaction/", FailedTransaction, name="failed_transaction"),
]
