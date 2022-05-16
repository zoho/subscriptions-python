from subscriptions.models import CustomField, Tag, Contactperson
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class CreditNote:

    @staticmethod
    def create(creditnote):
        ValidateDataType.class_name(creditnote, CreditNote)
        return RequestUtil.execute("POST", Resource.class_path(CreditNote()), creditnote)

    @staticmethod
    def emailAnCreditNote(creditnote_id, mail):
        ValidateDataType.class_name(mail, CreditNote.Mail)
        return RequestUtil.execute("POST", Resource.instance_path(CreditNote(), creditnote_id) + "/email", mail)

    @staticmethod
    def delete(creditnote_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(CreditNote(), creditnote_id))

    @staticmethod
    def convertToVoid(creditnote_id):
        return RequestUtil.execute("POST", Resource.instance_path(CreditNote(), creditnote_id) + "/void")

    @staticmethod
    def retrieve(creditnote_id):
        return RequestUtil.execute("GET", Resource.instance_path(CreditNote(), creditnote_id))

    @staticmethod
    def convertToOpen(creditnote_id):
        return RequestUtil.execute("POST", Resource.instance_path(CreditNote(), creditnote_id) + "/converttoopen")

    @staticmethod
    def applyToInvoice(invoices, creditnote_id):
        return RequestUtil.execute("POST", Resource.instance_path(CreditNote(), creditnote_id) + "/invoices", invoices)

    def set_amount(self, amount):
        self.amount = amount

    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id

    def set_reference_invoice_type(self,reference_invoice_type):
        self.reference_invoice_type=reference_invoice_type

    def set_gst_reason(self,gst_reason):
        self.gst_reason=gst_reason

    def set_creditnote_number(self, creditnote_number):
        self.creditnote_number = creditnote_number

    def set_contact_persons(self, contact_persons):
        ValidateDataType.class_name(contact_persons, list)
        self.contact_persons = contact_persons

    def set_date(self, date):
        self.date = date

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_creditnote_items(self,creditnote_items):
        ValidateDataType.list(creditnote_items, CreditNote.CreditnoteItems)
        self.creditnote_items=creditnote_items

    def set_custom_fields(self, custom_fields):
        ValidateDataType.list(custom_fields, CustomField)
        self.custom_fields = custom_fields

    def set_reference_number(self, reference_number):
        self.reference_number = reference_number

    def set_email(self, email):
        self.email = email

    def set_total(self, total):
        self.total = total

    def set_balance(self, balance):
        self.balance = balance

    def set_exchange_rate(self,exchange_rate):
        self.exchange_rate=exchange_rate

    def set_invoices(self,invoices):
        ValidateDataType.list(invoices, CreditNote.Invoices)
        self.invoices=invoices

    class CreditnoteItems:
        def set_item_id(self, item_id):
            self.item_id = item_id

        def set_description(self, description):
            self.description = description

        def set_code(self, code):
            self.code = code

        def set_account_id(self, account_id):
            self.account_id = account_id

        def set_quantity(self, quantity):
            self.quantity = quantity

        def set_tag(self, tag=[]):
            ValidateDataType.list(tag, Tag)
            self.tag = tag

        def set_item_custom_fields(self, item_custom_fields):
            ValidateDataType.list(item_custom_fields, CustomField)
            self.item_custom_fields = item_custom_fields

        def set_tax_id(self, tax_id):
            self.tax_id = tax_id

        def set_tax_exemption_id(self, tax_exemption_id):
            self.tax_exemption_id = tax_exemption_id

        def set_tax_exemption_code(self, tax_exemption_code):
            self.tax_exemption_code = tax_exemption_code

        def set_price(self, price):
            self.price = price

    def set_ignore_auto_number_generation(self, ignore_auto_number_generation):
        self.ignore_auto_number_generation = ignore_auto_number_generation

    def set_notes(self, notes):
        self.notes = notes

    def set_terms(self, terms):
        self.terms = terms

    def set_template_id(self, template_id):
        self.template_id = template_id

    class Mail:
        def set_to_mail_ids(self, to_mail_ids):
            ValidateDataType.class_name(to_mail_ids, list)
            self.to_mail_ids = to_mail_ids

        def set_cc_mail_ids(self, cc_mail_ids):
            ValidateDataType.class_name(cc_mail_ids, list)
            self.cc_mail_ids = cc_mail_ids

        def set_subject(self, subject):
            self.subject = subject

        def set_body(self, body):
            self.body = body

    class Invoices:
        def set_invoice_id(self, invoice_id):
            self.invoice_id = invoice_id

        def set_amount_applied(self, amount_applied):
            self.amount_applied = amount_applied
