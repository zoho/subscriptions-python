from subscriptions.models.Customer import Customer
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource


class BankAccount:
    @staticmethod
    def retrieve(customerId, AccountId):
        return RequestUtil.execute("GET",
                                   Resource.instance_path(Customer(), customerId) + "/bankaccounts/" + AccountId)

    @staticmethod
    def delete(customerId, AccountId):
        return RequestUtil.execute("DELETE",
                                   Resource.instance_path(Customer(), customerId) + "/bankaccounts/" + AccountId)

    def set_cvv_number(self, cvv_number):
        self.cvv_number = cvv_number

    def set_card_number(self, card_number):
        self.card_number = card_number

    def set_gateway(self, gateway):
        self.gateway = gateway

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_account_type(self, account_type):
        self.account_type = account_type

    def set_routing_number(self, routing_number):
        self.routing_number = routing_number

    def set_bank_name(self, bank_name):
        self.bank_name = bank_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_accept_license(self, accept_license):
        self.accept_license = accept_license

    def set_account_id(self, account_id):
        self.account_id = account_id

    def set_last_four_digits(self, last_four_digits):
        self.last_four_digits = last_four_digits

    def set_subscription_count(self, subscription_count):
        self.subscription_count = subscription_count

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_status(self, status):
        self.status = status
