from subscriptions import GenericParams
from subscriptions.net.GenericListParams import GenericListParams
from subscriptions.net.RequestUtil import RequestUtil
from subscriptions.net.Resource import Resource
from subscriptions.net.ValidateDataType import ValidateDataType


class Transaction:
    @staticmethod
    def list(parameter=GenericListParams()):
        if parameter is not None:
            ValidateDataType.tuples(parameter, (GenericParams, GenericListParams))
        return RequestUtil.execute("GET", Resource.class_path(Transaction()), None,
                                   parameter)
