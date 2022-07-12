from do_twice_decorator import print_name
from surprise import function_basic
from type_check import check_type
#*********************************************************************************************************************
if __name__ == '__main__':

    #surprise_decorator
    print(function_basic())

    #twice_decorator
    print_name()

    #type_check
    print(check_type(2))
    print( check_type("my exercise "))

#********************************************************************************************************************



