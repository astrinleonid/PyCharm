import argparse

def add(num1, num2):
    " Returns sum of two numbers "
    return num1 + num2

def subtract(num1, num2):
    " Returns difference of two numbers "
    return num1 - num2

def multiply(num1, num2):
    " Returns product of two numbers "
    return num1 * num2

def divide(num1, num2):
    " Returns quotient of two numbers "
    return num1 / num2

def perform_calculation(func, arg1, arg2):
    return func(arg1,arg2)


def command_calculator():
    """
    Processes three arguments from the command line: function, first_number, second_number
    Returns the result of application of the function to two numbers
    """
    AVAILABLE_FUNCTIONS = {'add':add, 'subtract':subtract, 'multiply':multiply,'divide':divide }

    parser = argparse.ArgumentParser()
 
    parser.add_argument("-w","--welcome", help="say Good Morning",
                        action="store_true")
    choises = [key for key in AVAILABLE_FUNCTIONS.keys()]
    parser.add_argument("function", type=str, choices=choises)
    parser.add_argument("first_number", type=int)
    parser.add_argument("second_number", type=int)
    args = parser.parse_args()
    if args.welcome:
        print('Good Morning:)')

    result = perform_calculation(AVAILABLE_FUNCTIONS[args.function],args.first_number,args.second_number)
    print(result)


if __name__ == '__main__' :
     command_calculator()