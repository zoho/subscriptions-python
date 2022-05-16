from subscriptions.models import Plan, CustomField, Tag
from subscriptions.net import GenericParams
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Addon:
    @staticmethod
    def retrieve(addon_id):
        return RequestUtil.execute("GET", Resource.instance_path(Addon(),addon_id))

    @staticmethod
    def list(params=GenericListParams()):
        ValidateDataType.tuples(params, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Addon()), None, params)

    @staticmethod
    def create(addon):
        ValidateDataType.class_name(addon, Addon)
        return RequestUtil.execute("POST", Resource.class_path(Addon()), addon)

    @staticmethod
    def update(addon, addon_id):
        ValidateDataType.class_name(addon, Addon)
        return RequestUtil.execute("PUT", Resource.instance_path(Addon(), addon_id), addon)

    @staticmethod
    def mark_as_active(addon_id):
        return RequestUtil.execute("POST", Resource.instance_path(Addon(), addon_id)+"/markasactive")

    @staticmethod
    def mark_as_inactive(addon_id):
        return RequestUtil.execute("POST", Resource.instance_path(Addon(), addon_id)+"/markasinactive")

    @staticmethod
    def delete(addon_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Addon(),addon_id))

    def set_name(self, name):
        self.name = name

    def set_addon_code(self, addon_code):
        self.addon_code = addon_code

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_account_id(self,account_id):
        self.account_id = account_id

    def set_account_name(self, account_name):
        self.account_name = account_name

    def set_applicable_to_all_plans(self, applicable_to_all_plans):
        self.applicable_to_all_plans = applicable_to_all_plans

    def set_plans(self, plans):
        ValidateDataType.list(plans, Plan)
        self.plans = plans

    def set_type(self, type):
        self.type = type

    def set_pricing_scheme(self, pricing_scheme):
        self.pricing_scheme = pricing_scheme

    def set_unit_name(self, unit_name):
        self.unit_name = unit_name

    def set_interval_unit(self, interval_unit):
        self.interval_unit = interval_unit

    def set_price_brackets(self, price_brackets):
        ValidateDataType.list(price_brackets, Addon.PriceBracket)
        self.price_brackets = price_brackets

    def set_tax_id(self, tax_id):
        self.tax_id = tax_id

    def set_tax_exemption_id(self, tax_exemption_id):
        self.tax_exemption_id = tax_exemption_id

    def set_tax_exemption_code(self, tax_exemption_code):
        self.tax_exemption_code = tax_exemption_code

    def set_is_taxable(self, is_taxable):
        self.is_taxable = is_taxable

    def set_tax_name(self, tax_name):
        self.tax_name = tax_name

    def set_tax_percentage(self, tax_percentage):
        self.tax_percentage = tax_percentage

    def set_tax_type(self, tax_type):
        self.tax_type = tax_type

    def set_product_type(self, product_type):
        self.product_type = product_type

    def set_addon_id(self, addon_id):
        self.addon_id = addon_id

    def set_status(self, status):
        self.status = status

    def set_created_time(self, created_time):
        self.created_time = created_time

    def set_updated_time(self, updated_time):
        self.updated_time = updated_time

    def set_show_in_widget(self, show_in_widget):
        self.show_in_widget = show_in_widget

    def set_show_in_portal(self, show_in_portal):
        self.show_in_portal = show_in_portal

    def set_description(self, description):
        self.description = description

    class PriceBracket:
        def set_start_quantity(self, start_quantity):
            self.start_quantity = start_quantity

        def set_end_quantity(self, end_quantity):
            self.end_quantity = end_quantity

        def set_price(self, price):
            self.price = price


    def set_custom_fields(self, custom_fields):
        ValidateDataType.list(custom_fields, CustomField)
        self.custom_fields = custom_fields

    def set_tags(self, tags):
        ValidateDataType.list(tags, Tag)
        self.tags = tags

