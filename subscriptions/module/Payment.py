from subscriptions.module import CustomField
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Payment:

    @staticmethod
    def create_payment(payment):
        ValidateDataType.class_name(payment, Payment)
        return RequestUtil.execute("POST", Resource.class_path(Payment()), payment)

    @staticmethod
    def update_payment(payment_id, payment):
        ValidateDataType.class_name(payment, Payment)
        return RequestUtil.execute("PUT", Resource.instance_path(Payment(), payment_id), payment)

    @staticmethod
    def retrieve_payment(payment_id):
        return RequestUtil.execute("GET", Resource.instance_path(Payment(), payment_id))

    @staticmethod
    def delete_payment(payment_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Payment(),payment_id))

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_payment_mode(self, payment_mode):
        self.payment_mode = payment_mode

    def set_amount(self, amount):
        self.amount = amount

    def set_date(self, date):
        self.date = date

    def set_reference_number(self,reference_number):
        self.reference_number = reference_number

    def set_description(self, description):
        self.description = description

    def set_invoices(self, invoices):
        ValidateDataType.list(invoices, Payment.Invoices)
        self.invoices = invoices

    class Invoices:
        def set_invoice_id(self, invoice_id):
            self.invoice_id = invoice_id

        def set_amount_applied(self, amount_applied):
            self.amount_applied = amount_applied

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def set_bank_charges(self, bank_charges):
        self.bank_charges = bank_charges

    def set_tax_account_id(self, tax_account_id):
        self.tax_account_id = tax_account_id

    def set_account_id(self, account_id):
        self.account_id = account_id

    def set_custom_fields(self, custom_fields):
        ValidateDataType.list(custom_fields, CustomField)
        self.custom_fields = custom_fields
