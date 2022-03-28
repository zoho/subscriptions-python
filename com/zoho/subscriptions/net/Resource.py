class Resource:
    @staticmethod
    def className(clazz):
        name = type(clazz).__name__.lower()
        return name + "s"

    @staticmethod
    def instancePath(clazz, id):
        return "%s/%s" % (Resource.classPath(clazz), id)

    @staticmethod
    def classPath(clazz):
        return Resource.className(clazz)

    @staticmethod
    def get_settings_path():
        return "settings/"
