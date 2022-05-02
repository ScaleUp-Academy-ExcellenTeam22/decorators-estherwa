from functools import wraps
#********************************************************************************************************************
def decorator_factory_funct(data_type):
    """
    This is a decorator that gets a type
    and must check if the var is an object that the function gets.
    :param data_type: The object type.
    :return: The decorator func
    """
    def decorator(function):
        """
        This decorator that checks if we get correct type.
        :param function:  receives one object.
        :return: A function.
        """
        @wraps(function)
        def type_check(obj):
            if not data_type(obj) == data_type:
                raise Exception("This is not the correct type")
            return function(obj)
        return type_check
    return decorator
#********************************************************************************************************************
@decorator_factory_funct(int)
def check_type(number):
        return number * 2
#********************************************************************************************************************

