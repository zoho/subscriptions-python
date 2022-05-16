from subscriptions.models import Coupon, Card, BankAccount, PaymentGateway
from subscriptions.net.GenericParams import GenericParams
from subscriptions.models import Customer, CustomField, Tag
from subscriptions.models.Contactperson import Contactperson
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Subscription:
    @staticmethod
    def create(subscription):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.class_path(Subscription()), subscription)

    @staticmethod
    def retrieve(subscription_id):
        return RequestUtil.execute("GET", Resource.instance_path(Subscription(), subscription_id))

    @staticmethod
    def list(params=GenericListParams()):
        ValidateDataType.tuples(params, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Subscription()), None, params)

    @staticmethod
    def get_recent_activities(subscription_id):
        return RequestUtil.execute("GET", Resource.instance_path(Subscription(), subscription_id) + "/recentactivities")

    @staticmethod
    def update(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("PUT", Resource.instance_path(Subscription(), subscription_id), subscription)

    @staticmethod
    def auto_charge(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/autocollect",
                                   subscription)

    @staticmethod
    def buy_one_time_addon(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/buyonetimeaddon",
                                   subscription)

    @staticmethod
    def cancel_end(subscription, subscription_id):
        subscription.set_cancel_at_end(True)
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/cancel",
                                   subscription)

    @staticmethod
    def cancel_now(subscription, subscription_id):
        subscription.set_cancel_at_end(False)
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/cancel",
                                   subscription)

    @staticmethod
    def update_card(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/card",
                                   subscription)

    @staticmethod
    def remove_card(subscription_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Subscription(), subscription_id) + "/card")

    @staticmethod
    def update_bank_account(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/bankaccount",
                                   subscription)

    @staticmethod
    def add_charge(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/charge",
                                   subscription)

    @staticmethod
    def add_contact_person(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Contactperson)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/contactpersons",
                                   subscription)

    @staticmethod
    def add_coupon(subscription_id, coupon_code):
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(),
                                                                  subscription_id) + "/" + Resource.instance_path(
            Coupon(), coupon_code))

    @staticmethod
    def reactivate(subscription_id):
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/reactivate")

    @staticmethod
    def postpone_renewal(renewal_at, subscription_id):
        subscription = Subscription()
        subscription.set_renewal_at(renewal_at)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/postpone",
                                   subscription)

    @staticmethod
    def delete_coupon(subscription_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Subscription(), subscription_id) + "/coupons")

    @staticmethod
    def delete(subscription_id):
        return RequestUtil.execute("DELETE", Resource.instance_path(Subscription(), subscription_id))

    @staticmethod
    def view_scheduled_changes(subscription_id):
        return RequestUtil.execute("GET", Resource.instance_path(Subscription(), subscription_id) + "/scheduledchanges")

    @staticmethod
    def add_or_edit_description_in_plan(description, subscription_id, plan_code):
        subscription = Subscription()
        subscription.set_description(description)
        return RequestUtil.execute("POST",
                                   Resource.instance_path(Subscription(), subscription_id) + "/lineitems/" + plan_code,
                                   subscription)

    @staticmethod
    def add_or_edit_description_in_addon(description, subscription_id, addon_code):
        subscription = Subscription()
        subscription.set_description(description)
        return RequestUtil.execute("POST",
                                   Resource.instance_path(Subscription(), subscription_id) + "/lineitems/" + addon_code,
                                   subscription)

    @staticmethod
    def update_reference(reference_id, subscription_id):
        subscription = Subscription()
        subscription.set_renewal_at(reference_id)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/reference",
                                   subscription)

    @staticmethod
    def update_salesperson(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/salesperson",
                                   subscription)

    @staticmethod
    def update_custom_field(subscription, subscription_id):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/customfields",
                                   subscription)

    @staticmethod
    def add_note(description, subscription_id):
        subscription = Subscription()
        subscription.set_description(description)
        return RequestUtil.execute("POST", Resource.instance_path(Subscription(), subscription_id) + "/notes",
                                   subscription)

    @staticmethod
    def delete_note(subscription_id, note_id):
        return RequestUtil.execute("DELETE",
                                   Resource.instance_path(Subscription(), subscription_id) + "/notes/" + note_id)

    def set_subscription_id(self, subscription_id):
        self.subscription_id = subscription_id

    def set_cancel_at_end(self, cancel_at_end):
        self.cancel_at_end = cancel_at_end

    def set_customer(self, customer):
        ValidateDataType.class_name(customer, Customer)
        self.customer = customer

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_payment_terms(self, payment_terms):
        self.payment_terms = payment_terms

    def set_payment_terms_label(self, payment_terms_label):
        self.payment_terms_label = payment_terms_label

    def set_custom_fields(self, custom_fields):
        ValidateDataType.list(custom_fields, CustomField)
        self.custom_fields = custom_fields

    def set_contactpersons(self, contactpersons):
        ValidateDataType.list(contactpersons, Contactperson)
        self.contactpersons = contactpersons

    def set_card_id(self, card_id):
        self.card_id = card_id

    def set_starts_at(self, starts_at):
        self.starts_at = starts_at

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def set_place_of_supply(self, place_of_supply):
        self.place_of_supply = place_of_supply

    def set_plan(self, plan):
        ValidateDataType.class_name(plan, Subscription.Plan)
        self.plan = plan

    def set_addons(self, addons):
        ValidateDataType.list(addons, Subscription.Addon)
        self.addons = addons

    def set_coupon_code(self, coupon_code):
        self.coupon_code = coupon_code

    def set_auto_collect(self, auto_collect):
        self.auto_collect = auto_collect

    def set_reference_id(self, reference_id):
        self.reference_id = reference_id

    def set_salesperson_name(self, salesperson_name):
        self.salesperson_name = salesperson_name

    def set_payment_gateways(self, payment_gateways):
        ValidateDataType.list(payment_gateways, PaymentGateway)
        self.payment_gateways = payment_gateways

    def set_create_backdated_invoice(self, create_backdated_invoice):
        self.create_backdated_invoice = create_backdated_invoice

    def set_can_charge_setup_fee_imemediately(self, can_charge_setup_fee_imemediately):
        self.can_charge_setup_fee_imemediately = can_charge_setup_fee_imemediately

    def set_template_id(self, template_id):
        self.template_id = template_id

    def set_is_metered_billing(self, is_metered_billing):
        self.is_metered_billing = is_metered_billing

    def set_salesperson_id(self, salesperson_id):
        self.salesperson_id = salesperson_id

    def set_end_of_term(self, end_of_term):
        self.end_of_term = end_of_term

    def set_add_to_unbilled_charges(self, add_to_unbilled_charges):
        self.add_to_unbilled_charges = add_to_unbilled_charges

    def set_amount(self, amount):
        self.amount = amount

    def set_description(self, description):
        self.description = description

    def set_tags(self, tags):
        ValidateDataType.class_name(tags, Tag)
        self.tags = tags

    def set_item_custom_fields(self, item_custom_fields):
        ValidateDataType.class_name(item_custom_fields, CustomField)
        self.item_custom_fields = item_custom_fields

    def set_account_id(self, account_id):
        self.account_id = account_id

    def set_renewal_at(self, renewal_at):
        self.renewal_at = renewal_at

    def set_card(self, card):
        ValidateDataType.class_name(card, Card)
        self.card = card

    def set_can_add_bank_account(self, can_add_bank_account):
        self.can_add_bank_account = can_add_bank_account

    def set_bank_account(self, bank_account):
        ValidateDataType.class_name(bank_account, BankAccount)
        self.bank_account = bank_account

    def set_created_at(self, created_at):
        self.created_at = created_at

    def set_unbilled_charge_id(self, unbilled_charge_id):
        self.unbilled_charge_id = unbilled_charge_id

    def set_can_charge_setup_fee_immediately(self, can_charge_setup_fee_immediately):
        can_charge_setup_fee_immediately = can_charge_setup_fee_immediately

    def set_reason(self, reason):
        self.reason = reason

    class Plan:
        def set_plan_code(self, plan_code):
            self.plan_code = plan_code

        def set_name(self, name):
            self.name = name

        def set_discount(self, discount):
            self.discount = discount

        def set_price(self, price):
            self.price = price

        def set_total(self, total):
            self.total = total

        def set_quantity(self, quantity):
            self.quantity = quantity

        def set_exclude_setup_fee(self, exclude_set_up_fee):
            self.exclude_setup_fee = exclude_set_up_fee

        def set_exclude_trial(self, exclude_trial):
            self.exclude_trial = exclude_trial

        def set_plan_description(self, plan_description):
            self.plan_description = plan_description

        def set_trial_days(self, trail_days):
            self.trial_days(trail_days)

        def set_billing_cycles(self, billing_cycles):
            self.billing_cycles = billing_cycles

        def set_setup_fee(self, set_up_fee):
            self.set_up_fee = set_up_fee

        def set_tax_exemption_id(self, tax_exemption_id):
            self.tax_exemption_id = tax_exemption_id

        def set_tax_exemption_code(self, tax_exemption_code):
            self.tax_exemption_code = tax_exemption_code

        def set_tax_id(self, tax_id):
            self.tax_id = tax_id

        def set_setup_fee_tax_id(self, setup_fee_tax_id):
            self.setup_fee_tax_id = setup_fee_tax_id

        def set_setup_fee_tax_exemption_id(self, setup_fee_tax_exemption_id):
            self.setup_fee_tax_exemption_id = setup_fee_tax_exemption_id

        def set_setup_fee_tax_exemption_code(self, setup_fee_tax_exemption_code):
            self.setup_fee_tax_exemption_code = setup_fee_tax_exemption_code

        def set_exclude_trial(self, exclude_trial):
            self.exclude_trial = exclude_trial

        def set_item_custom_fields(self, item_custom_fields):
            ValidateDataType.class_name(item_custom_fields, CustomField)
            self.item_custom_fields = item_custom_fields

        def set_tags(self, tags):
            ValidateDataType.class_name(tags, Tag)
            self.tags = tags

        def set_exclude_setup_fee(self, exclude_setup_fee):
            self.exclude_setup_fee = exclude_setup_fee

        def set_billing_cycles(self, billing_cycles):
            self.billing_cycles = billing_cycles

    class Addon:

        def set_addon_code(self, addon_code):
            self.addon_code = addon_code

        def set_addon_description(self, addon_description):
            self.addon_description = addon_description

        def set_price(self, price):
            self.price = price

        def set_quantity(self, quantity):
            self.quantity = quantity

        def set_tags(self, tags):
            ValidateDataType.class_name(tags, Tag)
            self.tags = tags

        def set_item_custom_fields(self, item_custom_fields):
            self.item_custom_fields = item_custom_fields

        def set_tax_id(self, tax_id):
            self.tax_id = tax_id

        def set_tax_exemption_id(self, tax_exemption_id):
            self.tax_exemption_id = tax_exemption_id

        def set_tax_exemption_code(self, tax_exemption_code):
            self.tax_exemption_code = tax_exemption_code
