import decorator

@decorator.decorator
def execute_double_decorator(function):
    """
    In this function we use the decorator in order to execute the function twice.
    :param function: The decorator of the function.
    """
    function()
    function()

    return function

@execute_double_decorator
def print_name():
    """
    We call the print function and use the decorator.
    """
    print("We are using the twice decorator")
