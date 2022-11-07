def get_numbers_from_user():
    """
    Prompts user to input several integers and
    returns the tuple containing all the numbers provided as integers
    """
    list_of_numbers = []
    while len(list_of_numbers) == 0:
        string = input("Please enter severl numbers separated with space (q for quit):")
        if string[0] == 'q':
            break
        list_of_numbers_as_strings = string.split()
        for item in list_of_numbers_as_strings:
            try:
                list_of_numbers.append(int(item))
            except:
                list_of_numbers = []
                print("Please provide a valid input")
                break
    return tuple(list_of_numbers)

def multiply_numbers(list_of_numbers):
    """
    Takes tuple containing several numbers and returns their product
    """
    product = 1
    for number in list_of_numbers:
        product *= int(number)
    return product

def multiply_numbers_from_string():
    """
    Prompts user to input several integers and
    returns the product of all the numbers provided
    """
    list_of_numbers = get_numbers_from_user()
    return multiply_numbers(list_of_numbers)

if __name__ == '__main__':
    assert multiply_numbers((2,-4,5)) == -40
    print(multiply_numbers_from_string())


