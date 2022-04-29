from subscriptions import GenericParams
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Currency:
    @staticmethod
    def list(parameter=GenericListParams()):
        if parameter is not None:
            ValidateDataType.tuples(parameter, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.get_settings_path() + Resource.class_path(Currency()), None, parameter)
