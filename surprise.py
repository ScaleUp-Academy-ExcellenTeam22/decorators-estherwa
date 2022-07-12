
def surprise_decorator_func(func: callable) :
    """
    Making a decorator that is going to print “Surprise!” instead of its original value.
    :param func: Function to call
    :return: The function that returns another string in this case Surprise.
    """
    def decorate():
        print( "Surprise!")
    return decorate

#********************************************************************************************************************
@surprise_decorator_func
def function_basic() :
    """
    Returning one string.
    :return: string.
    """
    return "print the function"
#********************************************************************************************************************
