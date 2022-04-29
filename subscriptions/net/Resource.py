class Resource:
    @staticmethod
    def class_name(clazz):
        name = type(clazz).__name__.lower()
        if name.endswith("y"):
            length = len(name)
            name = name[0:length - 1] + "ie"
        return name + "s"

    @staticmethod
    def instance_path(clazz, id):
        return "%s/%s" % (Resource.class_path(clazz), id)

    @staticmethod
    def class_path(clazz):
        return Resource.class_name(clazz)

    @staticmethod
    def get_settings_path():
        return "settings/"
