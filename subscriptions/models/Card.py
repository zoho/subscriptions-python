from subscriptions.models.Customer import Customer
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource


class Card:
    @staticmethod
    def retrieve(customerId, cardId):
        return RequestUtil.execute("GET", Resource.instance_path(Customer(), customerId) + "/cards/" + cardId)

    @staticmethod
    def delete(customerId, cardId):
        return RequestUtil.execute("DELETE", Resource.instance_path(Customer(), customerId) + "/cards/" + cardId)

    def set_card_id(self, cardId):
        self.card_id = cardId

    def set_status(self, status):
        self.status = status

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_last_four_digits(self, last_four_digits):
        self.last_four_digits = last_four_digits

    def set_expire_month(self, expire_month):
        self.expire_month = expire_month

    def set_expire_year(self, expire_year):
        self.expire_year = expire_year

    def set_card_number(self, card_number):
        self.card_number = card_number

    def set_cvv_number(self, cvv_number):
        self.cvv_number = cvv_number

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_country(self, country):
        self.country = country

    def set_zip(self, zip):
        self.zip = zip

    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def set_card_type(self, card_type):
        self.card_type = card_type

    def set_address(self, address):
        self.address = address

    def set_gateway_customer_id(self, gateway_customer_id):
        self.gateway_customer_id = gateway_customer_id

    def set_gateway_card_id(self, gateway_card_id):
        self.gateway_card_id = gateway_card_id

    def set_gateway_reference_id(self, gateway_reference_id):
        self.gateway_reference_id = gateway_reference_id
