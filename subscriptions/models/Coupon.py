from subscriptions.models import Plan, Addon
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.GenericParams import GenericParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Coupon:

    def set_name(self, name):
        self.name = name

    def set_coupon_code(self,coupon_code):
        self.coupon_code=coupon_code

    def set_description(self, description):
        self.description = description

    def set_max_redemption(self, max_redemption):
        self.max_redemption = max_redemption

    def set_expiry_at(self, expiry_at):
        self.expiry_at = expiry_at

    def set_type(self, type):
        self.type = type

    def set_duration(self, duration):
        self.duration = duration

    def set_discount_by(self, discount_by):
        self.discount_by = discount_by

    def set_discount_value(self, discount_value):
        self.discount_value = discount_value

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_apply_to_plans(self, apply_to_plans):
        self.apply_to_plans = apply_to_plans

    def set_plans(self, plans):
        ValidateDataType.list(plans, Plan)
        self.plans = plans

    def set_apply_to_addon(self, apply_to_addon):
        self.apply_to_addons = apply_to_addon

    def set_addon(self, addon):
        ValidateDataType.list(addon, Addon)
        self.addon = addon

    @staticmethod
    def create(coupon):
        ValidateDataType.class_name(coupon, Coupon)
        return RequestUtil.execute("POST", Resource.class_path(Coupon()), coupon)

    @staticmethod
    def list(parameter=GenericListParams()):
        ValidateDataType.tuples(parameter, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Coupon()), None, parameter)

    @staticmethod
    def delete(coupon_code):
        return RequestUtil.execute("DELETE", Resource.instance_path(Coupon(), coupon_code))

    @staticmethod
    def update(coupon, coupon_code):
        ValidateDataType.class_name(coupon, Coupon)
        return RequestUtil.execute("PUT", Resource.instance_path(Coupon(), coupon_code), coupon)

    @staticmethod
    def retrieve(coupon_code):
        return RequestUtil.execute("GET", Resource.instance_path(Coupon(), coupon_code), None, None)

    @staticmethod
    def mark_as_active(coupon_code):
        return RequestUtil.execute("POST", Resource.instance_path(Coupon(), coupon_code) + "/markasactive")

    @staticmethod
    def mark_as_inactive(coupon_code):
        return RequestUtil.execute("POST", Resource.instance_path(Coupon(), coupon_code) + "/markasinactive")

