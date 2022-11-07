def multiply_numbers():
    """
    Prompts user to input several integers and
    returns the product of all the numbers provided
    """
    string = input("Please enter the string:")
    list_of_numbers = string.split()
    product = 1
    for number in list_of_numbers:
        product *= int(number)
    return product


if __name__ == '__main__':
    print(multiply_numbers())


