
def multiply_string(string):
    """
    Takes the string as an argument and returns the string
    with every character of the original string duplicated
    """
    new_string = ""
    # string_list = list(str)
    for character in string:
        new_string += character * 2
    return new_string

def main():
    string = input("Please enter the string:")
    print(multiply_string(string))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
