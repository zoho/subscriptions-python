import sys


class TypeChecker:

    @staticmethod
    def class_name(instance,clazz):
        if isinstance(instance, clazz):
            return True
        raise TypeChecker.error(clazz)

    @staticmethod
    def tuples(instance, clazz):
        if isinstance(instance, clazz):
            return True
        message = clazz[0].__name__ + " or " + clazz[1].__name__
        raise TypeChecker.string(message)

    @staticmethod
    def list(instance,instance_type):
        if isinstance(instance,list):
            for value in instance:
                if not isinstance(value,instance_type):
                    raise TypeChecker.error(instance_type)
            return True
        raise TypeChecker.error(list)

    @staticmethod
    def error(clazz):
        sys.exit("Type mismatched:\nThe given instance is not of the type "+clazz.__name__)

    @staticmethod
    def string(message):
        sys.exit("Type mismatched:\nThe given instance is not of the type " + message)