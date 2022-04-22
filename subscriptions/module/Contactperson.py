from subscriptions.module import Customer
from subscriptions.net import GenericListParams, GenericParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Contactperson:

    @staticmethod
    def retrieve(customer_id, contactperson_id):
        return RequestUtil.execute("GET", Resource.instance_path(Customer(), customer_id)+"/"+ Resource.instance_path(Contactperson(), contactperson_id))

    @staticmethod
    def list(customer_id, params):
        if params is not None:
            ValidateDataType.tuples(params, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.instance_path(Customer(), customer_id)+"/"+Resource.class_path(Contactperson()), None, params)

    @staticmethod
    def create(customer_id, contactperson):
        return RequestUtil.execute("POST", Resource.instance_path(Customer(), customer_id)+"/"+Resource.class_path(Contactperson()), contactperson)

    @staticmethod
    def update(contactperson, customer_id, contactperson_id):
        return RequestUtil.execute("PUT", Resource.instance_path(Customer(), customer_id)+"/"+Resource.instance_path(Contactperson, contactperson_id), contactperson)

    @staticmethod
    def delete(customer_id, contactperson_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Customer, customer_id)+"/"+Resource.instance_path(Contactperson, contactperson_id))

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_mobile(self, mobile):
        self.mobile = mobile

    def set_contactperson_id(self, contactperson_id):
        self.contactperson_id = contactperson_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_created_time(self, created_time):
        self.created_time = created_time

    def set_updated_time(self, updated_time):
        self.updated_time = updated_time


