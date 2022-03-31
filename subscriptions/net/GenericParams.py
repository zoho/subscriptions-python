class GenericParams:
    _qParams = dict()

    def get_query_params(self):
        return self._qParams

    @staticmethod
    def set(key, value):
        GenericParams._qParams.update({key: value})
