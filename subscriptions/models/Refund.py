from subscriptions.models.CreditNote import CreditNote
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType
from subscriptions.models.Payment import Payment


class Refund:
    @staticmethod
    def refund_credit_note(creditnote_id, refund):
        ValidateDataType.class_name(refund, Refund)
        return RequestUtil.execute("POST", Resource.instance_path(CreditNote(), creditnote_id)+"/refunds", refund)

    @staticmethod
    def refund_payment(payment_id, refund):
        ValidateDataType.class_name(refund, Refund)
        return RequestUtil.execute("POST", Resource.instance_path(Payment(), payment_id)+"/refunds", refund)

    @staticmethod
    def retrieve_refund_details(refund_id):
        return RequestUtil.execute("GET", "creditnotes/"+Resource.instance_path(Refund(), refund_id))

    def set_amount(self, amount):
        self.amount = amount

    def set_description(self, description):
        self.description = description

