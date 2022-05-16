from subscriptions.models import Subscription
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Hostedpage:
    @staticmethod
    def retrieve(hostedpage_id):
        return RequestUtil.execute("GET", Resource.instance_path(Hostedpage(), hostedpage_id))

    @staticmethod
    def list():
        return RequestUtil.execute("GET", Resource.class_path(Hostedpage()))

    @staticmethod
    def createSubscription(subscription):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.class_path(Hostedpage()) + "/newsubscription", subscription)

    @staticmethod
    def updateSubscription(subscription):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.class_path(Hostedpage()) + "/updatesubscription", subscription)

    @staticmethod
    def updateCard(subscription):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.class_path(Hostedpage()) + "/updatecard", subscription)

    @staticmethod
    def buyOneTimeAddon(subscription):
        ValidateDataType.class_name(subscription, Subscription)
        return RequestUtil.execute("POST", Resource.class_path(Hostedpage()) + "/buyonetimeaddon", subscription)
