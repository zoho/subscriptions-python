from com.zoho.subscriptions.net.RequestUtil import RequestUtil
from com.zoho.subscriptions.net.Resource import Resource


class Plan:

    @staticmethod
    def retrieve(plan_code):
        return RequestUtil.execute("GET", Resource.instance_path(Plan(),plan_code))

    @staticmethod
    def list(params=None):
        return RequestUtil.execute("GET", Resource.class_path(Plan()), None, params)

    @staticmethod
    def create(plan):
        return RequestUtil.execute("POST", Resource.class_path(Plan()), plan)

    @staticmethod
    def mark_as_active(plan_code):
        return RequestUtil.execute("POST", Resource.instance_path(Plan(), plan_code) + "/markasactive")

    @staticmethod
    def mark_as_inactive( plan_code):
        return RequestUtil.execute("POST",Resource.instance_path(Plan(), plan_code)+"/markasinactive")

    @staticmethod
    def update(plan, plan_code):
        return RequestUtil.execute("PUT", Resource.instance_path(Plan(), plan_code), plan)

    @staticmethod
    def delete(plan_code):
        return RequestUtil.execute("DELETE", Resource.instance_path(Plan(), plan_code))

    def set_plan_code(self, plan_code):
        self.plan_code = plan_code

    def set_name(self, name):
        self.name = name

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_product_type(self, product_type):
        self.product_type = product_type

    def set_account_id(self, account_id):
        self.account_id = account_id

    def set_trial_kperiod(self, trial_period):
        self.trial_period = trial_period

    def set_setup_fee(self, setup_fee):
        self.setup_fee = setup_fee

    def set_recurring_price(self, recurring_price):
        self.recurring_price = recurring_price

    def set_interval(self, interval):
        self.interval = interval

    def set_interval_unit(self, interval_unit):
        self.interval_unit = interval_unit

    def set_billing_cycles(self, billing_cycles):
        self.billing_cycles = billing_cycles

    def set_tax_id(self, tax_id):
        self.tax_id = tax_id

    def set_is_taxable(self, is_taxable):
        self.is_taxable = is_taxable

    def set_tax_exemption_id(self, tax_exemption_id):
        self.tax_exemption_id = tax_exemption_id

    def set_tax_exemption_code(self, tax_exemption_code):
        self.tax_exemption_code = tax_exemption_code

    def set_show_in_widget(self, show_in_widget):
        self.show_in_widget = show_in_widget

    def set_show_in_protal(self, show_in_portal):
        self.show_in_portal = show_in_portal

    def set_description(self, description):
        self.description = description

    def set_tax_name(self, tax_name):
        self.tax_name = tax_name

    def set_tax_percentage(self, tax_percentage):
        self.tax_percentage = tax_percentage

    def set_tax_type(self, tax_type):
        self.tax_type = tax_type

    def set_status(self, status):
        self.status = status

    def set_created_time(self, created_time):
        self.created_time = created_time

    def set_updated_time(self, updated_time):
        self.updated_time = updated_time

    def set_addons(self, addons):
        self.addons = addons

    def set_customfields(self, customfields):
        self.customfields = customfields

    def set_tags(self, tags):
        self.tags = tags
