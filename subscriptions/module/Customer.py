from subscriptions import Tag, GenericParams
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Customer:

    def set_display_name(self, name):
        self.display_name = name

    def set_email(self, email):
        self.email = email

    def set_mobile(self, mobile):
        self.mobile = mobile

    def set_salutation(self, salutation):
        self.salutation = salutation

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_tag(self, tag=[]):
        ValidateDataType.list(tag, Tag)
        self.tag = tag

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_phone(self, phone):
        self.phone = phone

    def set_billing_address(self, billing_address):
        ValidateDataType.class_name(billing_address,Address)
        self.billing_address = billing_address

    def set_shipping_address(self, shipping_address):
        ValidateDataType.class_name(shipping_address, Address)
        self.shipping_address = shipping_address

    def set_fax(self, fax):
        self.fax = fax

    def set_currency_code(self, currency_code):
        self.currency_code = currency_code

    def set_twitter(self, twitter):
        self.twitter = twitter

    def set_facebook(self, facebook):
        self.facebook = facebook

    def set_skype(self, skype):
        self.skype = skype

    def set_is_portal_enabled(self, is_portal_enabled):
        self.is_portal_enabled = is_portal_enabled

    def set_gst_no(self, gst_no):
        self.gst_no = gst_no

    def set_gst_treatment(self, gst_treatment):
        self.gst_treatment = gst_treatment

    def set_place_of_contact(self, place_of_contact):
        self.place_of_contact = place_of_contact

    def set_vat_treatment(self, vat_treatment):
        self.vat_treatment = vat_treatment

    def set_vat_reg_no(self, vat_reg_no):
        self.vat_reg_no = vat_reg_no

    def set_is_taxable(self, is_taxable):
        self.is_taxable = is_taxable

    def set_tax_id(self, tax_id):
        self.tax_id = tax_id

    def set_tax_authority_id(self, tax_authority_id):
        self.tax_authority_id = tax_authority_id

    def set_tax_authority_name(self, tax_authority_name):
        self.tax_authority_name = tax_authority_name

    def set_tax_exemption_id(self, tax_exemption_id):
        self.tax_exemption_id = tax_exemption_id

    def set_tax_exemption_code(self, tax_exemption_code):
        self.tax_exemption_code = tax_exemption_code

    def set_default_templates(self, default_templates):
        ValidateDataType.list(default_templates, default_templates)
        self.default_templates = default_templates

    @staticmethod
    def create(customer):
        ValidateDataType.class_name(customer, Customer)
        return RequestUtil.execute("POST", Resource.class_path(Customer()), customer)

    @staticmethod
    def list(parameter=None):
        if parameter is not None:
            ValidateDataType.tuples(parameter, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Customer()), None, parameter)

    @staticmethod
    def delete(customer_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Customer(), customer_id))

    @staticmethod
    def update(customer, customer_id):
        ValidateDataType.class_name(customer, Customer)
        return RequestUtil.execute("PUT", Resource.instance_path(Customer(), customer_id), customer)

    @staticmethod
    def retrieve(customer_id):
        return RequestUtil.execute("GET", Resource.instance_path(Customer(), customer_id), None, None)

    @staticmethod
    def mark_as_active(customer_id):
        return RequestUtil.execute("POST", Resource.instance_path(Customer(), customer_id) + "/markasactive")

    @staticmethod
    def mark_as_inactive(customer_id):
        return RequestUtil.execute("POST", Resource.instance_path(Customer(), customer_id) + "/markasinactive")


class Address:
    def set_attention(self, attention):
        self.attention = attention

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

    def set_state_code(self, state_code):
        self.state_code = state_code

    def set_fax(self, fax):
        self.fax = fax


class default_templates:
    def set_invoice_template_id(self, template_id):
        self.invoice_template_id = template_id

    def set_creditnote_template_id(self, creditnote_template_id):
        self.creditnote_template_id = creditnote_template_id
