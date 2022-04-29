from subscriptions.net import GenericParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Product:
    @staticmethod
    def retrieve(product_id):
        return RequestUtil.execute("GET", Resource.instance_path(Product(), product_id))

    @staticmethod
    def list(params=None):
        if params is None:
            params = GenericParams()
        return RequestUtil.execute("GET", Resource.class_path(Product()), None, params)

    @staticmethod
    def create(product):
        ValidateDataType.class_name(product, Product)
        return RequestUtil.execute("POST", Resource.class_path(Product()), product)

    @staticmethod
    def update(product, product_id):
        ValidateDataType.class_name(product, Product)
        return RequestUtil.execute("PUT", Resource.instance_path(Product(), product_id), product)

    @staticmethod
    def mark_as_active(product_id):
        return RequestUtil.execute("POST", Resource.instance_path(Product(), product_id) + "/markasactive")

    @staticmethod
    def mark_as_inactive(product_id):
        return RequestUtil.execute("POST", Resource.instance_path(Product(), product_id) + "/markasinactive")

    @staticmethod
    def delete(product_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Product(), product_id))

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_redirect_url(self, redirect_url):
        self.redirect_url = redirect_url

    def set_email_ids(self, email_ids):
        self.email_ids = email_ids

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_status(self, status):
        self.status = status

    def set_created_time(self, created_time):
        self.created_time = created_time

    def set_updated_tim(self, updated_time):
        self.updated_time = updated_time

    def set_plans_count(self, plans_count):
        self.plans_count = plans_count

    def set_addons_count(self, addons_count):
        self.addons_count = addons_count

    def set_coupons_count(self, coupons_count):
        self.coupons_count = coupons_count
