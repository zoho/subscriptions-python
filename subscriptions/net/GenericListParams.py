from subscriptions.net.GenericParams import GenericParams


class GenericListParams(GenericParams):
    __defaultParams = None

    def __init__(self):
        self.set_page(1)
        self.set_per_page(200)

    def set_page(self, page):
        super()._qParams.update({"page": page})

    def set_per_page(self, per_page):
        super()._qParams.update({"per_page": per_page})

    def get_default(self):
        if self.__defaultParams is None:
            self.__defaultParams = GenericListParams()

        return self.__defaultParams
