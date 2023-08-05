"""This module defines a serializer for the transaction model."""
from rest_framework import serializers
from django.db.models import QuerySet

from polaris import settings
from polaris.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Defines the custom serializer for a transaction."""

    id = serializers.CharField()
    message = serializers.CharField()

    def __init__(self, data, *args, **kwargs):
        """
        Saves the transaction's asset to the object instance so _round_decimals()
        does not have to access instance.asset, making a new DB query each time.

        This class asssumes the transaction objects being passed use the same
        asset. If the transactions to be serialized are for multiple assets,
        split the calls to this serializer by asset.
        """
        if isinstance(data, Transaction):
            self.asset = data.asset
        elif isinstance(data, list) or isinstance(data, QuerySet):
            if isinstance(data, QuerySet):
                data = list(data)
            if len(data) != 0:
                self.asset = data[0].asset
        super().__init__(data, *args, **kwargs)

    def to_representation(self, instance):
        """
        Removes the "address" part of the to_address and from_address field
        names from the serialized representation. Also removes the
        deposit-related fields for withdraw transactions and vice-versa.
        """
        data = super().to_representation(instance)
        self._round_decimals(data, instance)
        data["to"] = data.pop("to_address")
        data["from"] = data.pop("from_address")
        if data["kind"] == Transaction.KIND.deposit:
            data["deposit_memo_type"] = data["memo_type"]
            data["deposit_memo"] = data["memo"]
        else:
            data["withdraw_memo_type"] = data["memo_type"]
            data["withdraw_memo"] = data["memo"]
            data["withdraw_anchor_account"] = data["receiving_anchor_account"]
            del data["claimable_balance_id"]
        if (
            instance.protocol == Transaction.PROTOCOL.sep6
            and not settings.SEP6_USE_MORE_INFO_URL
        ):
            del data["more_info_url"]
        del data["memo_type"]
        del data["memo"]
        del data["receiving_anchor_account"]
        return data

    def _round_decimals(self, data, instance):
        """
        Rounds each decimal field to instance.asset.significant_decimals.
        """
        for field in ["amount_in", "amount_out", "amount_fee"]:
            if getattr(instance, field) is None:
                continue
            data[field] = str(
                round(getattr(instance, field), self.asset.significant_decimals)
            )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "kind",
            "status",
            "status_eta",
            "amount_in",
            "amount_out",
            "amount_fee",
            "started_at",
            "completed_at",
            "stellar_transaction_id",
            "external_transaction_id",
            "from_address",
            "to_address",
            "receiving_anchor_account",
            "memo",
            "memo_type",
            "more_info_url",
            "refunded",
            "message",
            "claimable_balance_id",
        ]
