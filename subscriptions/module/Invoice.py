from subscriptions.module import CustomField
from subscriptions.net import GenericParams, GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Invoice:

    @staticmethod
    def retrieve(invoice_id):
        return RequestUtil.execute("GET", Resource.instance_path(Invoice(), invoice_id))

    @staticmethod
    def list(params=None):
        if params is not None:
            ValidateDataType.tuples(params, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Invoice()), None, params)

    @staticmethod
    def collect_via_bank(invoice_id, invoice):
        ValidateDataType.class_name(invoice, Invoice)
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id) + "/collect", invoice)

    @staticmethod
    def convert_to_void(invoice_id):
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id) + "/void", None, None)

    @staticmethod
    def convert_to_open(invoice_id):
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id) + "/converttoopen", None, None)

    @staticmethod
    def email_an_invoice(invoice_id, mail):
        ValidateDataType.class_name(mail, Invoice.Mail)
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/email", mail)

    @staticmethod
    def write_off(invoice_id):
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/writeoff", None, None)

    @staticmethod
    def cancel_write_off(invoice_id):
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/cancelwriteoff", None, None)

    @staticmethod
    def update_address(invoice_id, invoice):
        ValidateDataType.class_name(invoice, Invoice)
        return RequestUtil.execute("PUT", Resource.instance_path(Invoice(),invoice_id)+"/address", invoice)

    @staticmethod
    def update_custom_fields(invoice_id, invoice):
        ValidateDataType.class_name(invoice, Invoice)
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/customfields", invoice)

    @staticmethod
    def apply_multiple_credits_to_invoice(invoice_id, invoice):
        ValidateDataType.class_name(invoice, Invoice)
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/credits", invoice)

    @staticmethod
    def add_items_to_pending_invoice(invoice_id, invoice):
        ValidateDataType.class_name(invoice, Invoice)
        return RequestUtil.execute("POST", Resource.instance_path(Invoice(), invoice_id)+"/lineitems", invoice)

    @staticmethod
    def delete_items_from_pending_invoice(invoice_id, item_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Invoice(), invoice_id)+"/lineitems"+item_id, None, None)

    def set_invoice_items(self, invoice_items):
        ValidateDataType.list(invoice_items, Invoice.InvoiceItems)
        self.invoice_items = invoice_items

    def set_apply_creditnotes(self, apply_creditnotes):
        ValidateDataType.list(apply_creditnotes, Invoice.ApplyCreditNotes)
        self.apply_creditnotes = apply_creditnotes

    def set_custom_fields(self, custom_fields):
        ValidateDataType.list(custom_fields, CustomField)
        self.custom_fields = custom_fields

    def set_account_id(self, account_id):
        self.account_id = account_id

    def set_billing_address(self, billing_address):
        ValidateDataType.class_name(billing_address, Invoice.BillingAddress)
        self.billing_address = billing_address

    def set_shipping_address(self, shipping_address):
        ValidateDataType.class_name(shipping_address, Invoice.ShippingAddress)
        self.shipping_address = shipping_address

    class InvoiceItems:
        def set_code(self, code):
            self.code = code

        def set_product_id(self, product_id):
            self.product_id = product_id

        def set_name(self, name):
            self.name = name

        def set_description(self, description):
            self.description = description

        def set_price(self, price):
            self.price = price

        def set_quantity(self, quantity):
            self.quantity = quantity

        def set_tax_id(self, tax_id):
            self.tax_id = tax_id

        def set_tax_exemption_id(self, tax_exemption_id):
            self.tax_exemption_id = tax_exemption_id

    class ApplyCreditNotes:
        def set_creditnote_id(self, creditnote_id):
            self.creditnote_id = creditnote_id

        def set_amount_applied(self, amount_applied):
            self.amount_applied = amount_applied

    class BillingAddress:
        def set_city(self, city):
            self.city = city

        def set_state(self, state):
            self.state = state

        def set_zip(self, zip):
            self.zip = zip

        def set_country(self, country):
            self.country = country

        def set_fax(self, fax):
            self.fax = fax

    class ShippingAddress:
        def set_street(self, street):
            self.street = street

        def set_city(self, city):
            self.city = city

        def set_state(self, state):
            self.state = state

        def set_zip(self, zip):
            self.zip = zip

        def set_country(self, country):
            self.country = country

        def set_fax(self, fax):
            self.fax = fax

    class Mail:
        def set_to_mail_ids(self, to_mail_ids):
            self.to_mail_ids = to_mail_ids

        def set_cc_mail_ids(self, cc_mail_ids):
            self.cc_mail_ids = cc_mail_ids

        def set_subject(self, subject):
            self.subject = subject

        def set_body(self, body):
            self.body = body

